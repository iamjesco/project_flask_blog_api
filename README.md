# Basic Flask API with SQLALCHEMY
A basic version of a blog API using Flask with SqlAlchemy. Meaning of basic is that there's no use of Blueprints, routing classes or Swagger.
Just plain routing functions. 

### Tech

![](https://img.shields.io/static/v1?style=for-the-badge&label=Python&message=3.9&color=006600&logo=python)  
![](https://img.shields.io/static/v1?style=for-the-badge&label=Flask&message=2.0&color=006600&logo=jetbrains)   
![](https://img.shields.io/static/v1?style=for-the-badge&label=Pycharm&message=2021.3.2&color=006600&logo=pycharm)  
![](https://img.shields.io/static/v1?style=for-the-badge&label=Sqlite&message=3.0&color=006600&logo=sqlite)  

# Rest API
The REST API to the example app is described below

### Get all posts

**Request**

![](https://img.shields.io/static/v1?label=GET&message=/api/posts/&color=005599)

```text
curl -i -H 'Accept: application/json' http://localhost:5000/api/posts/
```

**Response**

```text
HTTP/1.1 200 OK
Content-Type: application/json

[]
```

### Create Post
**Request**

![](https://img.shields.io/static/v1?label=POST&message=/api/posts/&color=005599)

```text
HTTP/1.1 201 OK
Content-Type: application/json
```

```text
curl -i -H 'Accept: application/json' http://localhost:5000/api/v1/blog/posts/
```
```json
[
    {
        "content": "Lorem ipsum geripsum git got dumb dipsum",
        "pk": 1,
        "published": "2022-02-24T18:07:29.163078+00:00",
        "title": "The very first title"
    }
]
```

### Get post
**Request**

![](https://img.shields.io/static/v1?label=GET&message=/api/posts/<int:pk>/&color=005599)

```text
HTTP/1.1 200 OK
Content-Type: application/json
```

```text
curl -i -H 'Accept: application/json' http://localhost:5000/api/v1/blog/posts/<int:pk>/
```

**Response**

### Update post
**Request**

![](https://img.shields.io/static/v1?label=PUT&message=/api/posts/<int:pk>/&color=005599)

```text
HTTP/1.1 200 OK
Content-Type: application/json
```

```
curl -iH 'Accept: application/json' http://localhost:5000/api/v1/blog/posts/<int:pk>/
```
```json
[
    {
        "content": "Lorem ipsum geripsum git got dumb dipsum",
        "pk": 1,
        "published": "2022-02-24T18:07:29.163078+00:00",
        "title": "The very first title"
    }
]
```

### Delete post
**Request**

![](https://img.shields.io/static/v1?label=DELETE&message=/api/posts/<int:pk>/&color=005599)

```text
HTTP/1.1 204 OK
Content-Type: application/json
```

```text
curl -i -H 'Accept: application/json' http://localhost:5000/api/v1/blog/posts/<int:pk>/
```

**Response**
```text
no response
```

### Packages used

* [Flask-Sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
* [Marshmallow-Sqlalchemy](https://marshmallow-sqlalchemy.readthedocs.io/en/latest/)

### Notes

* Requirements.txt file is included
* The latest Marshmallow version (3.14.1) throws a type error: got an unexpected keyword argument 'strict'. The workaround is to install an older version (2.20.1)





