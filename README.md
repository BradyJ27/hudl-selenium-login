# hudl-selenium-login

_Note_: My local machine is running Windows 10, and Python 3.10.4, if you are running any other OS and/or version of Python, results may vary. 

## Setting Username and Password
The username and password are pulled from a file named "secrets.json", which lives in the base directory of the repository. To enter your own username/password, please update the file named "secrets.json" of the format:
```json
{
    "email": "YOUR_EMAIL_HERE",
    "password": "YOUR_PASSWORD_HERE"
}
```

## Creating the Virtual Environment
1. Create a virtual environment by running: `python -m venv hudl-login-venv`
1. Activate your virtual environment:
    - Windows: `.\hudl-login-venv\Scripts\activate.bat`
    - Mac/Linux: `./hudl-login-venv/Scripts/activate`
1. Upgrade pip: `python -m pip install --upgrade pip`
1. Install requirements: `python -m pip install -r requirements.txt`

## Running the Project
To run the project, run `python hudl-login.py` and the Unit Tests will run.

There are currently 2 Unit Tests, one to detect a successful login, and one to detect a failed login. If both tests succeed, you should see an output that looks similar to:

```sh
----------------------------------------------------------------------
Ran 2 tests in 25.524s

OK
```