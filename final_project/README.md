# Todo List 專案

這是一個使用 Django 框架開發的待辦事項管理系統。

## 功能特點

- 用戶註冊和登入系統
- 待辦事項的增刪改查
- 任務完成狀態管理
- 任務分類和優先級設置
- 回收站功能
- 用戶設置管理

## 技術棧

- Python 3.9
- Django 4.2
- SQLite 數據庫
- HTML/CSS
- Bootstrap 5

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

4. 運行數據庫遷移
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

- **任務管理**
  - 創建新任務
  - 編輯現有任務
  - 標記任務完成
  - 刪除任務（移至回收站）

- **回收站**
  - 查看已刪除的任務
  - 恢復刪除的任務
  - 永久刪除任務

- **用戶設置**
  - 修改個人資料
  - 自定義界面設置

## 開發者

- 作者：Polalalabear
- 專案：Web Programming 期末專案 