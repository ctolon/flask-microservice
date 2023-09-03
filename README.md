# Microservices with Docker and Flask

* This is a simple microservices project using `Docker` and `Flask`.

* For Frontend, `Jinja2` and `Bootstrap` is used.

* Secret keys are stored in a `.env` file and they are generated using with `generate_token.py` script.

* The project is divided into 4 microservices: `user`, `book`, `order` and `frontend`.

* All database migration can be done using `make-migrations.sh` script.

* All databases stored at `<service>/database` folder.

## User Microservice

* Default Port: `5000` and Default Host: `0.0.0.0`

* `/api/user/login` - `POST` - Login user - Body: `{"username": string, "password": string}`

* `/api/user/create` - `POST` - Create user - Body: `{"username": string, "password": string}`

* `/api/user/all` - `GET` - Get all users

* `/api/user/logout` - `Post` - Logout user

* `/api/user/get` - `GET` - Get Current user

* `/api/user/exists/<username>` - `GET` - Check if user exists - Path Parameters: `username (string)`

## Book Microservice

* Default Port: `5002` and Default Host: `0.0.0.0`

* `/api/book/all` - `GET` - Get all books

* `/api/book/create` - `POST` - Create book - Body: `{"name": string, "slug": string, "image": string, "price": integer}`

* `/api/book/get/<slug>` - `GET` - Get book by slug - Path Parameters: `slug (string)`

## Order Microservice

* Default Port: `5001` and Default Host: `0.0.0.0`. Also, it depends on `user` and `book` microservices.

* All of the endpoints require authentication except Get all order. Authentication is done using Authorization header as `Authorization: api_key`. Authorization header can be obtained from `/api/user/login` endpoint.

* `/api/order/all` - `GET` - Get all orders

* `/api/order/add-item` - `POST` - Add order - Body: `{"book_id": integer, "quantity": integer}` Also, it requires `Authorization` header.

* `/api/order/checkout` - `POST` - Checkout order of user - Also, it requires `Authorization` header.

* `/api/order/` - `GET` - Get open order - Also, it requires `Authorization` header.

## Frontend Microservice

* Default Port: `5003` and Default Host: `0.0.0.0`. Also, it depends on `user`, `order` and `book` microservices.

* You can access the frontend from `http://0.0.0.0:5003` address.

## How to run the application

* First, you need to install `docker` and `docker-compose` on your machine.

* Then you can run the application using `docker compose build && docker-compose up -d` command in `frontend` folder. For stopping the application, you can use `docker-compose down` command. For restarting the application, you can use `docker-compose restart` command.