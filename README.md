## Installing MySQL
Before installing the Python MySQL connector, MySQL must be installed locally (otherwise I got `pip` errors):
- On macOS: `brew install mysql`
- Note: doing `brew unlink mysql-connector-c` didn't fix the `pip` errors--if you already did, `brew unlink mysql-connector-c` and just install `mysql` 

Then, in virtual environment, do the following: 
- `pip install pymysql`
- `pip install mysqlclient`