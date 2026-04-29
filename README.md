# django-x

A simple microblogging application built with Django 6.0.3.

## Overview

This is a Twitter-like social media app where users can:
- Register and authenticate
- Create, edit, and delete posts (called "x")
- Upload photos with posts
- Search through posts

## Tech Stack

- **Framework**: Django 6.0.3
- **Database**: SQLite3
- **Frontend**: Bootstrap 5
- **Python**: 3.x

## Project Structure

```
my1st/
├── my1st/              # Django project settings
│   ├── settings.py     # Project configuration
│   ├── urls.py         # URL routing
│   └── wsgi.py         # WSGI entry point
├── xbyme/              # Main application
│   ├── models.py       # Database models
│   ├── views.py        # View functions
│   ├── forms.py        # Django forms
│   ├── urls.py         # App URL patterns
│   └── templates/      # App templates
├── templates/          # Base templates
│   └── registration/   # Auth templates
├── static/             # Static files
├── media/              # User-uploaded files
│   └── photos/         # Uploaded images
└── db.sqlite3          # SQLite database
```

## Models

### x (Post)
| Field | Type | Description |
|-------|------|-------------|
| user | ForeignKey | Link to Django User |
| text | TextField | Post content (max 240 chars) |
| photo | ImageField | Optional image upload |
| created_at | DateTime | Creation timestamp |
| updated_at | DateTime | Last modified timestamp |

## URL Patterns

| Path | View | Description |
|------|------|-------------|
| `/` | x_list | Home - list all posts |
| `/create/` | x_create | Create new post |
| `/<id>/edit/` | x_edit | Edit existing post |
| `/<id>/delete/` | x_delete | Delete post |
| `/register/` | register | User registration |
| `/search/` | x_search | Search posts |

## Setup & Run

1. **Install dependencies**:
   ```bash
   pip install django
   ```

2. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

3. **Start development server**:
   ```bash
   python manage.py runserver
   ```

4. **Create admin user** (optional):
   ```bash
   python manage.py createsuperuser
   ```

## Features

- ✅ User registration and login
- ✅ Create posts with optional photo
- ✅ Edit own posts
- ✅ Delete own posts
- ✅ Post search functionality
- ✅ Responsive Bootstrap UI
- ✅ Image uploads stored in media/photos/

## Templates

- `templates/layout.html` - Base layout with Bootstrap
- `templates/registration/login.html` - Login page
- `templates/registration/logged_out.html` - Logout confirmation
- `templates/registration/register.html` - Registration form
- `xbyme/templates/index.html` - Landing page
- `xbyme/templates/x_list.html` - Post feed
- `xbyme/templates/x_form.html` - Create/Edit form
- `xbyme/templates/x_delete_confirm.html` - Delete confirmation
