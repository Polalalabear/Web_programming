from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils import timezone
from datetime import date, datetime, timedelta
from .models import Task, UserSettings
from .forms import TaskForm, UserRegistrationForm
import json
from django.contrib.auth.models import User
from django.db import IntegrityError

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        # 檢查使用者名稱是否已存在
        if User.objects.filter(username=username).exists():
            messages.error(request, '使用者名稱已存在')
            return render(request, 'todo/register.html', {'username': username})
        
        # 檢查密碼是否相符
        if password != confirm_password:
            messages.error(request, '兩次輸入的密碼不相符')
            return render(request, 'todo/register.html', {'username': username})
        
        try:
            # 創建新使用者
            user = User.objects.create_user(username=username, password=password)
            # 創建使用者設定
            UserSettings.objects.create(user=user)
            messages.success(request, '註冊成功！請登入')
            return redirect('login')
        except IntegrityError:
            messages.error(request, '註冊失敗，請稍後再試')
            return render(request, 'todo/register.html', {'username': username})
            
    return render(request, 'todo/register.html')

@login_required
def todo_list(request):
    # 處理過期任務
    today = date.today()
    Task.objects.filter(user=request.user, date__lt=today, is_deleted=False).update(is_deleted=True)
    
    # 獲取未完成的任務
    tasks = Task.objects.filter(user=request.user, completed=False, is_deleted=False)
    # 分頁處理
    paginator = Paginator(tasks, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # 獲取已完成的任務
    completed_tasks = Task.objects.filter(user=request.user, completed=True, is_deleted=False)
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, '任務已成功新增！')
            return redirect('todo_list')
    else:
        form = TaskForm()
    
    return render(request, 'todo/todo_list.html', {
        'form': form,
        'tasks': page_obj,
        'completed_tasks': completed_tasks
    })

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, '任務已成功更新！')
            return redirect('todo_list')
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'todo/edit_task.html', {
        'form': form,
        'task': task
    })

@login_required
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    status = '完成' if task.completed else '取消完成'
    messages.success(request, f'任務已{status}！')
    return redirect('todo_list')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.is_deleted = True
    task.save()
    messages.success(request, '任務已移至垃圾桶！')
    return redirect('todo_list')

@login_required
def trash_bin(request):
    tasks = Task.objects.filter(user=request.user, is_deleted=True)
    return render(request, 'todo/trash.html', {
        'tasks': tasks
    })

@login_required
def restore_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.is_deleted = False
    task.save()
    messages.success(request, '任務已還原！')
    return redirect('trash_bin')

@login_required
def permanent_delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    messages.success(request, '任務已永久刪除！')
    return redirect('trash_bin')

@login_required
def settings_view(request):
    # 取得或建立使用者設定
    user_settings, created = UserSettings.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        idle_timeout = int(request.POST.get('idle_timeout', 900))
        user_settings.idle_timeout = idle_timeout
        user_settings.save()
        request.session['idle_timeout'] = idle_timeout
        messages.success(request, '設定已更新')
        return redirect('settings')

    # 取得目前設定值
    idle_timeout = user_settings.idle_timeout
    request.session['idle_timeout'] = idle_timeout
    return render(request, 'todo/settings.html', {
        'idle_timeout': idle_timeout
    })

@login_required
def batch_action(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        task_ids = json.loads(request.POST.get('task_ids', '[]'))
        
        if action == 'restore':
            Task.objects.filter(id__in=task_ids, user=request.user).update(is_deleted=False)
            messages.success(request, '已成功還原選取的任務')
            return redirect('todo_list')
        elif action == 'delete':
            Task.objects.filter(id__in=task_ids, user=request.user).update(is_deleted=True)
            messages.success(request, '已成功將選取的任務移至垃圾桶')
            return redirect('todo_list')
        elif action == 'restore_trash':
            Task.objects.filter(id__in=task_ids, user=request.user).update(is_deleted=False)
            messages.success(request, '已成功還原選取的任務')
            return redirect('trash_bin')
        elif action == 'delete_trash':
            Task.objects.filter(id__in=task_ids, user=request.user).delete()
            messages.success(request, '已成功永久刪除選取的任務')
            return redirect('trash_bin')
            
    return redirect('todo_list')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # 設置閒置超時時間
            user_settings, created = UserSettings.objects.get_or_create(user=user)
            request.session['idle_timeout'] = user_settings.idle_timeout
            return redirect('todo_list')
        else:
            messages.error(request, '使用者名稱或密碼錯誤')
    return render(request, 'todo/login.html')

def handler404(request, exception):
    return render(request, 'todo/404.html', status=404)
