# ✅ Flask Task Manager App

A professional-level **Flask web application** for user authentication and task management. This project allows users to register, log in, and manage their daily tasks through a simple and clean dashboard interface.

---

## 🚀 Features

- 🔐 User Registration & Login
- 📋 Create & Manage Tasks
- 📅 Assign Due Dates
- 🔎 Search Tasks by Title
- 🧼 Clean UI with Template Inheritance
- 💾 SQLite Database with SQLAlchemy ORM
- ✅ Secure Password Hashing
- 🧩 Flask Blueprints for modular design

---

## 🛠 Tech Stack

- **Python 3.x**
- **Flask**
- **Flask-Login**
- **Flask-WTF**
- **SQLite**
- **Jinja2 Templates**

---

## 📁 Project Structure

project/
│
├── app/
│ ├── init.py
│ ├── models.py
│ ├── routes.py
│ ├── forms.py
│
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── login.html
│ ├── register.html
│ └── dashboard.html
│
├── run.py
├── .gitignore
└── README.md



---

## 🔧 Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/flask-task-manager.git
cd flask-task-manager

#Create and Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


#Install Dependencies
pip install -r requirements.txt

#Run the Application
python run.py
