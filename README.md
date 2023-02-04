# api_final_Yatube
[![Python](https://img.shields.io/badge/-Python-464641?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-464646?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![Pytest](https://img.shields.io/badge/Pytest-464646?style=flat-square&logo=pytest)](https://docs.pytest.org/en/6.2.x/)
[![Postman](https://img.shields.io/badge/Postman-464646?style=flat-square&logo=postman)](https://www.postman.com/)
## Описание:
api final Yatube — это блог-платформа Yatube.
Позволяет зарегистрированным пользователям:
- просматривать и опубликовывать посты
- просматривать группы
- подписываться на авторов
- оставлять комментарии к постам
- удалять посты
- удалять комментарии
- редактировать пост
- редактировать комментарии


## Как запустить проект (Windows):

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Timur-x/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate 
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Перейти в директорию api_final_yatube/yatube_api:

```
cd yatube_api
```

Выполнить миграции:

```
python manage.py makemigrations
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
## Примеры запросов:
### Создание пользователя:
```
  [POST].../api/v1/users/
  {
"username": "string",
"password": "string"
}
```
### Ответ:
```
{
    "email": "",
    "username": "st",
    "id": 1
}
```
### Получение JWT-токена:
```
    [POST].../api/v1/jwt/refresh/
    {
"refresh": "string",
"access": "string"
}
```

### Ответ:
```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3NTM1ODY0MCwianRpIjoiYzY3ZjVmZmUyZDljNDI5MDkyM2U5NzMwNmNkYzY0YzIiLCJ1c2VyX2lkIjoxf4.pxEQb-s3gwYib0zEGyRkOda6zwjeeP4RjlDN58Mq2oM",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc1MzU4NjQwLCJqdGkiOiI5M2ViMjQyMmU4YmM0MTY5OTM0MGY5ZmEyZWNiZjA4MSIsInVzZXJfaWQbOjF9._jYOFqR4MeQH7cGAuoavc-V914_5B1u3NFTpax54s4I"
}
```
### Запрос на создание публикации:
### но сначало надо передать токен "access"
- в заголовке указав `Authorization`:`Bearer <токен>`.


```
    [GET].../api/v1/posts/
    {
"text": "string",
"image": "string",
"group": 0
}
```
### Пример ответа:
```
    {
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}
```

### Подробная документация в формате ReDoc доступна по адресу .../redoc/
