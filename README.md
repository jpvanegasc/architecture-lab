# Architecture Lab
This project contains an implementation of the [RealWorld project](https://github.com/gothinkster/realworld) backend in different architectures, to compare and contrast the differences between them. It uses Python with FastAPI for the backend framework and Postgres with SQLAlchemy for the database.

### 📖 Table Of Contents
- 👀 [Overview](#-overview)
- 🪨 [Monolith](#-monolith)

## 👀 Overview
Following the RealWorld project idea the API for any architecture should work exactly the same, and can be tested using the Postman collection in `tests/`. Each architecture implementation is dockerized, exposing the API at [http://localhost:8000](http://localhost:8000), after which you can run the tests using `make test`.

## 🪨 Monolith
This implementation consists of a single container running the Python app, which handles all logic within it. It's built modularly, with each module handling a subset of the functionality.
