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

blog_api/                  
├── blog/                   
│   ├──__init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py          
│   ├── serializers.py      
│   ├── views.py           
│   ├── urls.py            
│   └── migrations/         
├── blog_api/               
│   ├──__init__.py
│   ├── asgi.py
│   ├── settings.py         
│   ├── urls.py             
│   └── wsgi.py
├── manage.py              
├── requirements.txt


##  Project Demo
<img width="1828" height="900" alt="1" src="https://github.com/user-attachments/assets/1454eba7-7494-4f2a-914e-93f6ad664ce8" />
<img width="1402" height="775" alt="2" src="https://github.com/user-attachments/assets/a925562f-41d8-4693-921b-464dc3b1a8c6" />
<img width="1637" height="891" alt="3" src="https://github.com/user-attachments/assets/8c7c18c8-e99f-4ad5-8f64-71705e45229a" />
<img width="1375" height="856" alt="4" src="https://github.com/user-attachments/assets/9599644f-29b7-44c5-9fa5-50a4fd6eae76" />
<img width="1365" height="855" alt="5" src="https://github.com/user-attachments/assets/5928934b-9d8b-40f2-99e5-448ae4bd4a51" />
<img width="1579" height="883" alt="6" src="https://github.com/user-attachments/assets/9a5500b8-0e04-47ca-b5b7-3d62d1aef433" />
<img width="1375" height="833" alt="7" src="https://github.com/user-attachments/assets/aa814ce8-822f-455e-b9b8-e85fc46d83a5" />
<img width="1374" height="819" alt="8" src="https://github.com/user-attachments/assets/63ce310f-0ef2-45d8-8da1-77c9c26db7d9" />
<img width="1369" height="822" alt="9" src="https://github.com/user-attachments/assets/7e4ee368-f12b-439f-ae56-4680c745db27" />
