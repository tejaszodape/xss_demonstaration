# 🕵️‍♂️ XSS Demo App – Educational Cross-Site Scripting Playground

A safe, educational Django application that **demonstrates common XSS (Cross-Site Scripting) vulnerabilities** and how to prevent them. Built for learning purposes only.

> ⚠️ **This app intentionally contains security flaws. Do NOT use in production.**

---

## 🎯 Purpose

- Illustrate **Reflected**, **Stored**, and **DOM-based XSS** scenarios  
- Show the impact of unsafe user input handling  
- Demonstrate secure coding practices (e.g., escaping, CSP, validation)

---

## 🛠️ Tech Stack

- **Backend**: Python 3.8+, Django 4.x  
- **Database**: SQLite (zero setup)  
- **Frontend**: HTML, CSS, vanilla JavaScript  
- **Security Tools**: Demonstrates Django’s built-in protections (and how bypassing them causes XSS)

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/your-username/xss-demo-app.git
cd xss-demo-app
```
### 2 .Set up virtual environment
```
python -m venv venv
source venv/bin/activate    # Linux/macOS
 or
venv\Scripts\activate       # Windows
```

### 3 Install dependencies
```
pip install -r requirements.txt
```
### 4 Run migrations & start server
```
python manage.py migrate
python manage.py runserver
```

### 5 Visit in your browser
Open http://127.0.0.1:8000

Try harmless test payloads like:
html
```
<script>alert("XSS!")</script>
<img src="x" onerror="alert('Stored XSS')">
```
🔒 All examples are sandboxed, non-destructive, and reset on server restart.

### 🧪 Vulnerability Examples Included

| Type        | Location     | Description                                              |
|-------------|--------------|----------------------------------------------------------|
| Reflected   | `/search/`   | Unsafe rendering of URL query parameters                 |
| Stored      | `/guestbook/`| User comments saved and displayed without sanitization   |
| DOM-based   | `/profile/`  | Client-side JavaScript uses `innerHTML` with unsanitized input |
