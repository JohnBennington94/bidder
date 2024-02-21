# Setting up Postgres DB 🐘

## Initial Postgres setup 🚀
```
1. Run docker-compose up -d
2. Navigate to http://localhost:5050/
3. Log in using the credentials PGADMIN_DEFAULT_EMAIL and PGADMIN_DEFAULT_PASSWORD in compose
4. Right click on servers > register > server
5. Enter name for local server
6. Enter the following in 'Connection' tab
```

### Connection Properties 🔗

```
Host name      : postgres
Port           : 5432
Maintenance db : postgres
User           : admin
Password       : root
```

Then create the `BIDDER` database

## Upgrade Database ⬆️

If you make model changes in [bidder/models](../bidder/models.py) file

### Create migration scripts and apply to database 🛂
Then from 'bidsite' directory
* Make Migrations: `python manage.py makemigrations bidder`
* Run Migrations: `python manage.py migrate`
