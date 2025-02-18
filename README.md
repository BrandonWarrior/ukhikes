# Hiking Blog

## Overview

The **Hiking Blog** is a platform for outdoor enthusiasts to share, discover, and engage with hiking experiences. Users can create posts about their adventures, upvote or comment on other posts, and filter hikes by location and difficulty. The application is designed to be fully responsive and accessible across all devices.

For project planning, see: [Project Planning](planning.md)

---

## Features

### Core Features (MVP)

1. **User Registration and Authentication**:
   - Secure user registration and login.
   - Profile updates for showcasing user information and authored posts.

2. **Post Management**:
   - Create, edit, and delete posts with details like title, content, location, and difficulty.
   - Filter and search posts by location and difficulty.

3. **Community Interaction**:
   - Comment on posts to engage with the community.
   - Upvote/downvote posts to highlight the best content.

4. **Responsive Design**:
   - Fully responsive UI for desktop, tablet, and mobile devices.

5. **Admin Moderation**:
   - Admins can manage posts, comments, and users to maintain a positive community environment.

For a full list of planned features refer to the [Project Planning](planning.md) document.

---

## Installation and Setup

### Prerequisites

- Python 
- pip
- Virtual environment 

### Installation Steps

---

## 🐛 **Bugs and Fixes**

### **1️⃣ ERR_SSL_PROTOCOL_ERROR when Running the Server**
- **Bug**: Attempted to access Django’s development server over HTTPS, but it only supports HTTP.
- **Fix**: Used `http://127.0.0.1:8000/blog/` instead of `https://`.

---

### **2️⃣ Git Push Rejected Due to Upstream Issues**
- **Bug**: The local Git branch was behind the remote repository.
- **Fix**:
  - Pulled remote changes first using:
    ```bash
    git pull origin main --rebase
    ```
  - Then retried the push:
    ```bash
    git push origin main
    ```

---

### **3️⃣ Login Page Displaying "Register" Instead of "Login"**
- **Bug**: Incorrectly named template file or incorrect context variable.
- **Fix**:
  - Updated `login.html` template to correctly display "Login" instead of "Register."
  - Ensured the title block was set properly:
    ```html
    {% block title %}Login{% endblock %}
    ```

---

### **4️⃣ Unable to Login Using Email Instead of Username**
- **Bug**: Django-allauth defaulted to username-based authentication.
- **Fix**:
  - Enabled email-based login in `settings.py`:
    ```python
    ACCOUNT_AUTHENTICATION_METHOD = "email"
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_USERNAME_REQUIRED = False
    ```

---

### **5️⃣ Register Page Only Showing Footer**
- **Bug**: Missing `{% block content %}` in `register.html`, preventing the form from rendering.
- **Fix**:
  - Wrapped the content inside `{% block content %}` in `register.html`:
    ```html
    {% extends "base.html" %}

    {% block content %}
    <h2>Register</h2>
    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Sign Up</button>
    </form>
    {% endblock %}
    ```

---

### **6️⃣ `TemplateDoesNotExist: base.html` Error**
- **Bug**: Django couldn’t find `base.html` because it was placed in the wrong directory.
- **Fix**:
  - Moved `base.html` to the global `/templates/` directory.
  - Updated `settings.py` to reference the correct template path:
    ```python
    TEMPLATES = [
        {
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
        },
    ]
    ```

---

### **8️⃣ Virtual Environment (`env/`) Accidentally Tracked in Git**
- **Bug**: The virtual environment was committed to Git, causing conflicts during deployment.
- **Fix**:
  - Added `env/` to `.gitignore`:
    ```bash
    echo "env/" >> .gitignore
    ```
  - Removed it from Git:
    ```bash
    git rm -r --cached env/
    ```

---

### **9️⃣ Static Files Not Loading on Heroku**
- **Bug**: Static files were not properly collected and served in production.
- **Fix**:
  - Configured `STATICFILES_DIRS` and `STATIC_ROOT` in `settings.py`:
    ```python
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    ```
  - Ran `collectstatic`:
    ```bash
    heroku run python manage.py collectstatic --noinput
    ```

---

### **9️⃣ Static Files Not Loading on Heroku**
- **Bug**: Users could register but were unable to log in, both locally and on the deployed version. The issue was caused by missing authentication backends in settings.py, which prevented Django-Allauth from properly verifying user credentials.

- - **Fix**: Added the required authentication backends in settings.py:
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

---


## Credits
