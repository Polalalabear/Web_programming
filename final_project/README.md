# Todo List 專案

這是一個使用 Django 框架開發的待辦事項管理系統，提供直觀的使用者介面和完整的功能。

## 功能特點

- 用戶註冊和登入系統
  - 安全的密碼加密
  - 使用者名稱和密碼驗證
  - 自動登出功能（可設定閒置時間）
- 待辦事項的增刪改查
  - 新增待辦事項
  - 編輯待辦事項內容
  - 刪除待辦事項（移至回收站）
  - 查看待辦事項列表
- 任務完成狀態管理
  - 標記任務為已完成
  - 標記任務為未完成
  - 查看任務完成狀態
- 任務分類和優先級設置
  - 設定任務優先級
  - 任務分類管理
- 回收站功能
  - 查看已刪除的任務
  - 恢復刪除的任務
  - 永久刪除任務
- 用戶設置管理
  - 修改個人資料
  - 自定義界面設置
  - 設定自動登出時間

## 使用技術

- Python 3.9
- Django 4.2
- SQLite 資料庫
- HTML5/CSS3
- Bootstrap 5
- Font Awesome 5
- JavaScript

## 安裝說明

1. 克隆專案
```bash
git clone https://github.com/Polalalabear/Web_programming.git
cd Web_programming/final_project
```

2. 創建並激活虛擬環境
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
# 或
venv\Scripts\activate  # Windows
```

3. 安裝依賴
```bash
pip install -r requirements.txt
```

4. 運行資料庫遷移
```bash
python manage.py migrate
```

5. 啟動開發服務器
```bash
python manage.py runserver
```

## 使用說明

1. 訪問 http://localhost:8000 進入網站
2. 註冊新帳號或使用現有帳號登入
3. 開始管理你的待辦事項

## 主要功能

### 任務管理
- **新增任務**
  - 設定任務標題
  - 添加任務描述
  - 設定優先級
  - 選擇分類

- **編輯任務**
  - 修改任務內容
  - 更新優先級
  - 更改分類
  - 更新完成狀態

- **任務列表**
  - 查看所有任務
  - 按優先級排序
  - 按分類篩選
  - 搜尋任務

### 回收站
- 查看已刪除的任務
- 恢復刪除的任務
- 永久刪除任務
- 清空回收站

### 用戶設置
- 修改個人資料
- 自定義界面設置
- 設定自動登出時間
- 更改密碼

## 安全性功能
- 密碼加密存儲
- CSRF 保護
- 會話管理
- 自動登出機制

## 使用者介面
- 響應式設計
- 直觀的導航
- 美觀的圖示
- 清晰的視覺層次

## 開發者

- 作者：Polalalabear
- 專案：Web Programming 期末專案
- GitHub：[專案連結](https://github.com/Polalalabear/Web_programming/tree/main/final_project)

## 授權

本專案採用 MIT 授權條款。詳見 [LICENSE](LICENSE) 檔案。

## 管理員設置

### 創建管理員帳號
1. 進入 Django shell：
```bash
python3 manage.py shell
```

2. 創建管理員帳號：
```python
from django.contrib.auth.models import User
User.objects.create_superuser('admin', 'admin@example.com', '你的密碼')
```

3. 訪問管理界面：
- 網址：http://localhost:8000/admin/
- 使用創建的管理員帳號登入

### 管理員功能
- 查看所有用戶
- 管理所有任務
- 查看用戶設置
- 系統管理 

    ```bash
    # 初始化數據庫
    python3 manage.py migrate

    # 創建管理員帳號
    python3 manage.py createsuperuser
    ```
