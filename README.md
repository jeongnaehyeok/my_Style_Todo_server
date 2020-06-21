# my_Style_Todo_server

> Django-Rest-Framework project

## Client

### [My_Style_Todo](https://github.com/jeongnaehyeok/my_Style_Todo)

## Build Setup

```bash
# 패키지 설치
$ pip install -r requirements.txt
# 마이그래이션
$ python manage.py makemigrations
$ python manage.py migrate
# 실행
python manage.py runserver 127.0.0.1:8000 --insecure
```

## API

### Todos

#### Register

##### method : get

##### Url : api/todos/

##### Response:

```json
[
  {
    "id":int,
    "todo":string
  }
]
```

#### Update

##### method : put

##### Url : api/todos/\<todo id:int>/

##### Response:

```json
{
    "id":int,
    "todo":string
}
```

#### Delete

##### method : delete

##### Url : api/todos/\<todo id:int>/

##### Response:

```json

```

### 