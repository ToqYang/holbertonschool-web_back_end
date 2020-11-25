<p>
<img width="260" height="170" src="https://www.flaticon.com/svg/static/icons/svg/1205/1205526.svg" align="right" >
</p>

# :colombia: 0x09. Unittests and Integration Tests

## Prerequisites

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 `(version 3.7)`
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style `(version 2.5)`
- All your files must be executable
- All your modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`
- All your classes should have a documentation `(python3 -c 'print(__import__("my_module").MyClass.__doc__)')`
- All your functions (inside and outside a class) should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated.

## Run

```
$ python -m unittest path/to/test_file.py
```

## Files

| Files              | Description       |
| ------------------ | ----------------- |
| **README.md**      | Documentation     |
| **utils.py**       | Utilities         |
| **client.py**      | Clients           |
| **fixtures.py**    | Fixtures          |
| **test_utils.py**  | Reporting utils   |
| **test_client.py** | Reporting clients |
