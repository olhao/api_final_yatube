# api_final_yatube 🛫 ⛅ 🛬
***
api_final_yatube is DRF project which consists of posts and api apps.
Posts app includes models for db;
Api app includes urlpatterns, views (ModelViewSet), serializers.
The main idea of the api_final_yatube is:
> * to give opportunity to get authentication with JWTAuthentication;
> * to get, create, update and delete post/posts with IsAuthenticatedOrReadOnly permission (get list of posts paginated with LimitOffsetPagination);
> * to get, create, update and delete comment/comments to post with IsAuthenticatedOrReadOnly permission;
> * to get group/groups with IsAuthenticatedOrReadOnly permission;
> * to follow user, get list of followings and perform search with following name with IsAuthenticated permission.


### setup and run 🛠 :
***
clone the repo and CD in CLI 
```
git clone https://github.com/olhao/api_final_yatube.git
```
```
cd api_final_yatube
```

create and activate virtual environment 
```
python -m venv env
```
```
source env/bin/activate
```
```
python -m pip install --upgrade pip
```

setup dependences from file requirements.txt 
```
pip install -r requirements.txt
```

perform migrations 
```
python manage.py makemigrations
```
```
python manage.py migrate
```

run the project 
```
python manage.py runserver
```

### examples for Posts with Postman 💡
***
```
POST http://127.0.0.1:8000/api/v1/posts/
```

![img.png](img.png)

```
GET http://127.0.0.1:8000/api/v1/posts/158/
```

![img_1.png](img_1.png)

```
PATCH http://127.0.0.1:8000/api/v1/posts/158/
```

![img_2.png](img_2.png)

```
GET http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=2 with pagination
```

![img_3.png](img_3.png)

```
PUT http://127.0.0.1:8000/api/v1/posts/158/
```

![img_4.png](img_4.png)

```
DELETE http://127.0.0.1:8000/api/v1/posts/158/
```

![img_5.png](img_5.png)


Couple Negative scenarios:

```
DELETE already deleted post with id to get 404 status
```

![img_6.png](img_6.png)

```
PATCH already deleted post with id to get 404 status
```

![img_7.png](img_7.png)

```
PATCH the post that created with another user
```

![img_8.png](img_8.png)

