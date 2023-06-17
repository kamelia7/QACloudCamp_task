### Автоматизация тестирования API
Проект с автотестами, которые будут проверять работу всех API-эндпоинтов, описанных ниже:

* API url https://jsonplaceholder.typicode.com/
* Методы, требующие проверки: GET /posts, POST /posts, DELETE /posts
* Методы могут принимать параметры userId, id, title, body
* В качестве языка программирования используется python
* Используются библиотеки requests, а также pytest.

### Запуск

1. Клонируем репозиторий:

```git clone https://github.com/kamelia7/QACloudCamp_task```

2. Запускаем через docker-compose из папки проекта:

```docker-compose up```