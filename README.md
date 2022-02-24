# Basic Flask API with SQLALCHEMY
A basic version of a blog API using Flask with SqlAlchemy and Sqlite3. The standard 5 endpoints available:  

### Tech

![](https://img.shields.io/static/v1?style=social&label=Python&message=3.9&color=006600&logo=python)  
![](https://img.shields.io/static/v1?style=social&label=Flask&message=2.0&color=006600&logo=jetbrains)   
![](https://img.shields.io/static/v1?style=social&label=Pycharm&message=2021.3.2&color=006600&logo=pycharm)  
![](https://img.shields.io/static/v1?style=social&label=Sqlite&message=3.0&color=006600&logo=sqlite)  

# Rest API
The REST API to the example app is described below

### Get all posts

**Request**

![](https://img.shields.io/static/v1?label=GET&message=/api/posts/&color=005599)

```
curl -iH 'Accept: application/json' http://localhost:5000/api/v1/blog/posts/
```

### Create Post
**Request**

![](https://img.shields.io/static/v1?label=POST&message=/api/posts/&color=005599)

```
curl -iH 'Accept: application/json' http://localhost:5000/api/v1/blog/posts/
```
### Get post
**Request**

![](https://img.shields.io/static/v1?label=GET&message=/api/posts/<int:pk>/&color=005599)

```
curl -iH 'Accept: application/json' http://localhost:5000/api/v1/blog/posts/<int:pk>/
```

### Update post
**Request**

![](https://img.shields.io/static/v1?label=PUT&message=/api/posts/<int:pk>/&color=005599)

```
curl -iH 'Accept: application/json' http://localhost:5000/api/v1/blog/posts/<int:pk>/
```
### Delete post
**Request**

![](https://img.shields.io/static/v1?label=DELETE&message=/api/posts/<int:pk>/&color=005599)

```
curl -iH 'Accept: application/json' http://localhost:5000/api/v1/blog/posts/<int:pk>/
```

### Packages used

* Flask-Sqlalchemy
* Flask-Marshmallow
* Marshmallow-Sqlalchemy

### Notes

* Requirements.txt file is included
* The latest Marshmallow version (3.14.1) throws a type error: got an unexpected keyword argument 'strict'. The workaround is to install an older version (2.20.1)





