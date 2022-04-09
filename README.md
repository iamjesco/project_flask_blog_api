# Basic Flask API with SQLALCHEMY
A basic version of a blog API using Flask with SqlAlchemy. Meaning of basic is that there's no use of Blueprints, routing classes or Swagger.
Just plain routing functions. 

## Tech

![](https://img.shields.io/static/v1?style=for-the-badge&label=Python&message=3.9&color=006600&logo=python)  
![](https://img.shields.io/static/v1?style=for-the-badge&label=Flask&message=2.0&color=006600&logo=jetbrains)   
![](https://img.shields.io/static/v1?style=for-the-badge&label=Pycharm&message=2021.3.2&color=006600&logo=pycharm)  
![](https://img.shields.io/static/v1?style=for-the-badge&label=Sqlite&message=3.0&color=006600&logo=sqlite)  

## Get all posts

**Request**

![](https://img.shields.io/static/v1?label=GET&message=/api/posts/&color=005599)

```text
curl -i -H 'Accept: application/json' http://localhost:5000/api/posts/
```

**Response**

```text
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{
    "pk": 1,
    "title": "title",
    "slug": "slug",
    "author": "foo",
    "featured": false,
    "created": "date",
    "updated": "date"
}
```

## Create Post
**Request**

![](https://img.shields.io/static/v1?label=POST&message=/api/posts/&color=005599)
```text
curl -i -H 'Accept: application/json' http://localhost:5000/api/posts/
```
**Response**
```text
HTTP/1.1 201 OK
Content-Type: application/json
```
```json
{
    "title": "Foo",
    "body": "<p>Bar</p>"
}
```

## Get single post
**Request**

![](https://img.shields.io/static/v1?label=GET&message=/api/posts/<int:pk>/&color=005599)
```text
curl -i -H 'Accept: application/json' http://localhost:5000/api/posts/:pk
```
**Response**
```text
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{
    "pk": 1,
    "title": "title",
    "slug": "slug",
    "author": "foo",
    "featured": false,
    "created": "date",
    "updated": "date"
}
```

## Update post
**Request**

![](https://img.shields.io/static/v1?label=PUT&message=/api/posts/:pk&color=005599)
```text
curl -i -H 'Accept: application/json' http://localhost:5000/api/posts/:pk
```
**Response**
```text
HTTP/1.1 200 OK
Content-Type: application/json
```
* Since it's a Patch request each item can be updated individually (except update date)
```json
{
    "pk": 1,
    "title": "title",
    "slug": "slug",
    "author": "foo",
    "featured": false,
    "created": "date"
}
```

## Delete post
**Request**

![](https://img.shields.io/static/v1?label=DELETE&message=/api/posts/<int:pk>/&color=005599)
```text
curl -i -H 'Accept: application/json' http://localhost:5000/api/posts/:pk
```
```text
HTTP/1.1 204 OK
Content-Type: application/json
```

**Response**
```text
[]
```

## Additional packages used

* [Flask-Sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
* [Marshmallow-Sqlalchemy](https://marshmallow-sqlalchemy.readthedocs.io/en/latest/)
* [Psycopg](https://www.psycopg.org/)  // PostgreSQL adapter for the Python programming language
* [Gunicorn](https://gunicorn.org/)  // Python WSGI HTTP Server for UNIX

### Notes

* Requirements.txt file is included
* The latest Marshmallow version (3.14.1) throws a type error: got an unexpected keyword argument 'strict'. The workaround is to install an older version (2.20.1)
* For some reason I can't get the Postgress python adapter to work on m1 mac. 





