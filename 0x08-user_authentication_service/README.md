<p>
<img width="260" height="170" src="https://www.flaticon.com/svg/static/icons/svg/627/627558.svg" align="right" >
</p>

# :colombia: 0x08. User authentication service

- How to declare API routes in a Flask app
- How to get and set cookies
- How to retrieve request form data
- How to return various HTTP status codes

## Prerequisites

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`
- All your classes should have a documentation `(python3 -c 'print(__import__("my_module").MyClass.__doc__)')`
- All your functions (inside and outside a class) should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)'`
  and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions should be type annotated
- The flask app should only interact with `Auth` and never with `DB` directly.
- Only public methods of `Auth` and `DB` should be used outside these classes

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

## Setup

```
$ pip3 install -r requirements.txt
- requests
- flask
- pycodestyle2.5
```

## Run

```
$ ython3.7 ./app.py
```

## Routes

- `GET /`: Index
- `POST /users`: Register user {email: email, password: password}
- `POST /sessions`: Logged Post {email: email, password: password}
- `DELETE /sessions`: Destroy session
- `GET /profile`: Get user profile {session_id: 2345676543sdfghjgfd}
- `PUT /reset_password`: Reset the password {"email": email, "reset_token": token, "new_password": new_pwd}

## Files

| Files          | Description            |
| -------------- | ---------------------- |
| **0-main.py**  | User Initial           |
| **user.py**    | User model             |
| **1-main.py**  | Add user               |
| **2-main.py**  | Find user              |
| **3-main.py**  | Update user            |
| **4-main.py**  | Hash Password          |
| **db.py**      | Database methods       |
| **5-main.py**  | Register user          |
| **8-main.py**  | Credentials validation |
| **10-main.py** | Get session ID         |
| **auth.py**    | Authentication         |
| **app.py**     | Principal Main Flask   |
| **main.py**    | Test with assert       |
