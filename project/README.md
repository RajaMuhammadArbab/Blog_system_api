#  Django Blog RESTful API

A simple Django-based RESTful API for a blog system, supporting full CRUD operations and JWT authentication.

---

##  Features

- Create, Read, Update, Delete blog posts
- Author field for each post
- JWT authentication (login, refresh tokens)
- SQLite database (can be swapped)
- Token-protected routes
- Proper error handling (404, 401, etc.)

---

##  Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/blog-api.git
cd blog-api
```

### 2. Create virtual environment & install dependencies
```bash
python -m venv venv
source venv/bin/activate  
pip install -r requirements.txt
```

### 3. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create a superuser (for admin access)
```bash
python manage.py createsuperuser
```

### 5. Run the server
```bash
python manage.py runserver
```

---

##  Testing the API with Postman or Curl

###  1. Obtain Token

**POST** `/api/token/`

**Body:**
```json
{
  "username": "your_username",
  "password": "your_password"
}
```

**Response:**
```json
{
  "access": "ACCESS_TOKEN",
  "refresh": "REFRESH_TOKEN"
}
```

---

###  2. Refresh Token

**POST** `/api/token/refresh/`

**Body:**
```json
{
  "refresh": "REFRESH_TOKEN"
}
```

---

###  Blog Post Endpoints

All endpoints below require the `Authorization` header:

```
Authorization: Bearer ACCESS_TOKEN
```

---

####  Create a post

**POST** `/posts/`

**Body:**
```json
{
  "title": "My First Blog Post",
  "content": "This is the content of the blog.",
  "author": 1
}
```

---

####  Get all posts

**GET** `/posts/`

---

####  Get a specific post

**GET** `/posts/1/`

---

####  Update a post

**PUT** `/posts/1/`

**Body:**
```json
{
  "title": "Updated Title",
  "content": "Updated content.",
  "author": 1
}
```

---

####  Delete a post

**DELETE** `/posts/1/`

---

##  Technologies Used

- Python 3
- Django
- Django REST Framework
- Simple JWT
- SQLite (default)

---

##  Project Structure

```
blog_api/                  
├── blog/                   
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py          
│   ├── serializers.py      
│   ├── views.py           
│   ├── urls.py            
│   └── migrations/         
├── blog_api/               
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py         
│   ├── urls.py             
│   └── wsgi.py
├── manage.py              
├── requirements.txt       
             

