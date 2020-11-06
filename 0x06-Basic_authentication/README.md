<p>
<img width="260" height="170" src="https://www.flaticon.com/svg/static/icons/svg/627/627558.svg" align="right" >
</p>

# :colombia: 0x06. Basic authentication

- What authentication means
- What Base64 is
- How to encode a string in Base64
- What Basic authentication means
- How to send the Authorization header

## Prerequisites

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`
- All your classes should have a documentation `(python3 -c 'print(__import__("my_module").MyClass.__doc__)')`
- All your functions (inside and outside a class) should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'prin- (__import__("my_module").MyClass.my_function.__doc__)')`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

# Simple API

Simple HTTP API for playing with `User` model.

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints

## Setup

```
$ pip3 install -r requirements.txt
```

## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3.7 -m api.v1.app
```

## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)

## Files

| Files                | Description                                  |
| -------------------- | -------------------------------------------- |
| **requirements.txt** | Requeriments                                 |
| **models**           | Models                                       |
| **main_0.py**        | Auth class                                   |
| **main_1.py**        | Define which routes don't need authenticatio |
| **main_2.py**        | Basic - Base64 part                          |
| **main_3.py**        | Basic - Base64 decode                        |
| **main_4.py**        | Basic - User credentials                     |
| **main_5.py**        | Basic - User object                          |
| **main_6.py**        | Basic - Overload current_user - and BOOM!    |
| **main_100.py**      | Basic - Allow password with ":"              |
| **api**              | Flask                                        |
