# NOTES

#### Setting up virtual environment
- Clone the repo
- Create the virtual environment: `virtualenv venv`
- Activate virtual environment: `source venv/bin/activate`
- Install packages: `pip install -r requirements.txt`
- Make sure environment is set up: `./venv_test.py`
- Anything `pip` installs will be reflected in venv; `pip freeze > requirements.txt` to update
- Deactivate it when finished: `deactivate`

#### Installing MySQL
Before installing the Python MySQL connector, MySQL must be installed locally (otherwise I got `pip` errors):
- On macOS: `brew install mysql`
- Note: doing `brew unlink mysql-connector-c` didn't fix the `pip` errors--if you already did, `brew unlink mysql-connector-c` and just install `mysql` 

Then, in virtual environment, do the following: 
- `pip install pymysql`
- `pip install mysqlclient`