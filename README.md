#Instructions to use the code

This python program generates the random number and stores the value to the mysql backend database, so that the random number is unique.

1. Mysql standard DB installation.
2. Create database and table with desired names
3. Create .env file to store the mysql connection details as follows
HOSTNAME=<mysql host>
USERNAME=<username>
PASSWORD=<password>
DATABASE=<database>
TABLENAME=<table> 
4. Pull all the project files from github repo
5. Run following command to install required modules
$ pip install -r requirements.txt
6. Run Following command to run the webapp
$python webapp.py