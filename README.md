# Django Data - Project 

## To run this project

Clone this repo

Move to the folder  django-dataproject-shriya

Create a virtual environment and activate it:
```bash
virtualenv venv
source venv/bin/activate
```

Install all dependencies

```bash
pip3 install -r requirements.txt
```

<hr>

### To create databse and tables

In *.env* file put down the username and password of your postgres.

Then run the following command:

```bash  
python3 manage.py create_db
python3 manage.py migrate
```
<hr>

### To load data into the tables

```bash  
python3 manage.py data_insertion
```

<hr>

### Now that the Database is set,

Run the following command:
```bash
python3 manage.py runserver
```

<hr>

### To delete the Database

```bash  
python3 manage.py drop_db
```
