# Ecommerce Using Django Oscar

E-Commerce Template for Django Using Django Oscar

| Package  | Version |
|----------|---------|
| Python   | 3.11.xx |
| Django   | 5.0.10  |
| Postgres | 15.xx+  |


## Local setup

 - Set up the [python interpreter](#python-interpreter-setup), [.env file](#env-setup) and [postgres DB](#postgres-setup)
 - Run below commands along with path to .env

    ``` shell script
    python manage.py migrate
    python manage.py runserver
    ```
   

### Python interpreter setup
```shell script
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

### .env setup
 - Create the oscar_custom/.env file and copy the content from "oscar_custom/.env.example"
 - Update the oscar_custom/.env file with your credentials

### Postgres setup
 - Download and install postgres 15.xx from https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
 - Create a database
