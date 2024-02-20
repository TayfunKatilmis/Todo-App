# Django Restful Api
A simple todo app using django rest framework. 

# Futures
- User Auth. with jwt
- Forget password functionally.
- CRUD operations on `Task Model`.
- Application is dockerized with `docker-compose.yml` and `Dockerfile`.

# My Development Environment
- Python version: 
``` 
Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
```
# Environment Setup
Follow these steps to be sure your environment is acceptable for the project. I assume that you have docker installed in your system.
- Install libraries in requirements.txt
    - `pip install -r requirements.txt`
- Create your SQL database for Docker:
Run the following commands to create migrations and apply them to your database:
    - `docker-compose run web python manage.py makemigrations`
    - `docker-compose run web python manage.py migrate`
- Thats it! Sit back and enjoy docker magic after running these command:
    - `docker-compose up`