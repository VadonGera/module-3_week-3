# Документация API для приложения управления пользователями

Это API предоставляет возможность управления пользователями. 
С помощью этого API можно получать информацию о пользователях, создавать новых пользователей, 
обновлять их данные и удалять существующих.

### Модель `User`


```python
class User(BaseModel):
    id: int
    username: str
    wallet: Optional[float] = 0.0
    birthdate: date
```
* `id` — уникальный идентификатор пользователя.
* `username` — имя пользователя.
* `wallet` — баланс пользователя.
* `birthdate` — дата рождения пользователя.

### Эндпоинты


<table>
    <tr>
        <th>Method</th>
        <th>URL</th>
        <th>Body</th>
        <th>Query params</th>
        <th>Response</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>GET</td>
        <td>/users</td>
        <td></td>
        <td>sort_by, reverse, limit, offset</td>
        <td>[User]</td>
        <td>Получение списка всех пользователей</td>
    </tr>
    <tr>
        <td>GET</td>
        <td>/users/{user_id}</td>
        <td></td>
        <td></td>
        <td>User</td>
        <td>Получить пользователя по его ID</td>
    </tr>
    <tr>
        <td>POST</td>
        <td>/users</td>
        <td>User</td>
        <td></td>
        <td>User</td>
        <td>Создание нового пользователя</td>
    </tr>
    <tr>
        <td>PUT</td>
        <td>/users/{user_id}</td>
        <td>User</td>
        <td></td>
        <td>User</td>
        <td>Обновление данных пользователя</td>
    </tr>
    <tr>
        <td>DELETE</td>
        <td>/users/{user_id}</td>
        <td></td>
        <td></td>
        <td>User</td>
        <td>Удаление пользователя по его ID</td>
    </tr>
</table>


* Параметры запроса:
1. Сортировка
    * `sort_by: str` (default = None) - поле для сортировки списка
(указывается атрибут из модели User). 
При значении None, сортировка не выполняется.
    * `reverse: bool` (default = False) - направление сортировки: 
False - по возрастанию 'abc', True - по убыванию 'desc'. 
2. Пагинация
    * `limit: int` (default = 10) - количество выводимых записей в списке.
    * `offset: int` (default = 0) - запись, с которой начинается вывод списка.

> Важно! Перед выводом списка сначала выполняется сортировка, а потом пагинация. 

### Запуск

`uvicorn main:app --reload`

### Страница документации

`http://127.0.0.1:8000/docs`




![img.png](../../week_3/python_REST_API/img.png)

### Примеры
### 1. Получить первых 2-х пользователей из списка

```python
curl -X 'GET' \
  'http://127.0.0.1:8000/users?limit=2&offset=0' \
  -H 'accept: application/json'
```

Request URL
```python
http://127.0.0.1:8000/users?limit=2&offset=0
```
	
Response body
```python
[
  {
    "id": 1,
    "username": "Вадим",
    "wallet": 10,
    "birthdate": "1990-01-01"
  },
  {
    "id": 2,
    "username": "Eric",
    "wallet": 200,
    "birthdate": "1982-05-15"
  }
]
```

### 2. Получить список, отсортированный по убыванию поля `wallet` из 3-х пользователей, начиная со 2-й записи 

```python
curl -X 'GET' \
  'http://127.0.0.1:8000/users?sort_by=wallet&reverse=true&limit=3&offset=1' \
  -H 'accept: application/json'
```

Request URL
```python
http://127.0.0.1:8000/users?sort_by=wallet&reverse=true&limit=3&offset=1
```
Response body

```python
[
  {
    "id": 4,
    "username": "Kurt",
    "wallet": 2000,
    "birthdate": "1975-02-17"
  },
  {
    "id": 2,
    "username": "Eric",
    "wallet": 200,
    "birthdate": "1982-05-15"
  },
  {
    "id": 3,
    "username": "Gera",
    "wallet": 50,
    "birthdate": "1995-06-12"
  }
]
```

### 3. Получить пользователя по ID

```python
curl -X 'GET' \
  'http://127.0.0.1:8000/users/4' \
  -H 'accept: application/json'
```

Request URL
```python
http://127.0.0.1:8000/users/4
```

Response body
```python
{
  "id": 4,
  "username": "Kurt",
  "wallet": 2000,
  "birthdate": "1975-02-17"
}
```

### 4. Добавить нового пользователя

```python
curl -X 'POST' \
  'http://127.0.0.1:8000/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 10,
  "username": "Артур",
  "wallet": 120,
  "birthdate": "2001-04-12"
}'
```

Request URL

```python
http://127.0.0.1:8000/users/
```
Request body
```python
{
  "id": 10,
  "username": "Артур",
  "wallet": 120,
  "birthdate": "2001-04-12"
}
```
	
Response body

```python
{
  "id": 10,
  "username": "Артур",
  "wallet": 120,
  "birthdate": "2001-04-12"
}
```

### 5. Обновление данных пользователя

```python
curl -X 'POST' \
  'http://127.0.0.1:8000/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 1111111111,
  "username": "Artur",
  "wallet": 100,
  "birthdate": "2001-04-12"
}'
```

Request URL

```python
http://127.0.0.1:8000/users/10
```
Request body
```python
{
  "id": 1111111111,
  "username": "Artur",
  "wallet": 100,
  "birthdate": "2021-04-12"
}
```
	
Response body

```python
{
  "id": 10,
  "username": "Artur",
  "wallet": 100,
  "birthdate": "2021-04-12"
}
```

> Изменение атрибута `id` не влияет на изменение этого атрибута в базе данных.

### 6. Удаление пользователя по его ID

```python
curl -X 'DELETE' \
  'http://127.0.0.1:8000/users/10' \
  -H 'accept: application/json'
```

Request URL

```python
http://127.0.0.1:8000/users/10
```
	
Response body

```python
{
  "id": 10,
  "username": "Artur",
  "wallet": 100,
  "birthdate": "2021-04-12"
}
```

### Ошибки

При возникновении ошибок сервер возвращает соответствующий 
HTTP статус-код и сообщение об ошибке в формате JSON.

```python
curl -X 'DELETE' \
  'http://127.0.0.1:8000/users/10' \
  -H 'accept: application/json'
```

Request URL

```python
http://127.0.0.1:8000/users/10
```

`status_code` = 404

Response body
```python
{
  "detail": "Пользователь не найден"
}
```