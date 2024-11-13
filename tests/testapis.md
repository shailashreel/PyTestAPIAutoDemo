### Introduction of demo test API

#### Get API

- HOST: https://jsonplaceholder.typicode.com
- API path: /posts/1
- Request method: GET
- Request Parameters: None
- Request header: "Content-Type": "application/json; charset=utf-8"
- Request Body: None
- Response status code: 200
- Response header: "Content-Type": "application/json; charset=utf-8"
- Response body:

```json
{
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}
```

#### Post API

- HOST: https://jsonplaceholder.typicode.com
- API path:/posts
- Request method: POST
- Request Parameters: None
- Request header:"Content-Type": "application/json; charset=utf-8"
- Request Body:raw json format
- Request Body:

```json
{
    "title": "foo",
    "body": "bar",
    "userId": 1
}
```

- Response status code: 201
- Response header:"Content-Type": "application/json; charset=utf-8"
- Response body:

```json
{
    "title": "foo",
    "body": "bar",
    "userId": 1,
    "id": 101
}
```