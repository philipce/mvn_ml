# NOTES

#### Setting up virtual environment
- Clone the repo
- Create the virtual environment: `virtualenv venv`
- Activate virtual environment: `source venv/bin/activate`
- Install packages: `pip install -r requirements.txt`
- Make sure environment is set up: `./test_venv.py`
- Anything `pip` installs will be reflected in venv; `pip freeze > requirements.txt` to update
- Deactivate it when finished: `deactivate`

#### Installing MySQL
Before installing the Python MySQL connector, MySQL must be installed locally (otherwise I got `pip` errors):
- On macOS: `brew install mysql`
- Note: `brew install mysql-connector-c` didn't fix the `pip` errors--if you already did, `brew unlink mysql-connector-c` and just install `mysql` 

Then, in virtual environment, install a python mysql package: 
- `pip install pymysql` (`import pymysql`) or `pip install mysqlclient` (`import MySQLdb`)
- Note: kept having different issues arise with mysqlclient; recommend pymysql instead