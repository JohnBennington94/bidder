# Bidder 🚀

👋 Welcome to the Bidder application!

### Project Links 🔗

🪧 [Trello Board](https://trello.com/b/uZFCO5r6/bidder)<br>
📖 [User Stories](https://docs.google.com/spreadsheets/d/1J1wrD8q644g1r12xRZbP26m6NDapoj9c2mpidA5BrAE/edit#gid=0)

## Dev Setup 💻

### Setup Postgres Database 🐘

[Database setup](postgres_db/README.md) gives steps to create the database for bidder

### Run application on specific port 🏃🏻

`python manage.py runserver 8000`

### Create Admin User

`python manage.py createsuperuser` & follow prompts

### Google Cloud ☁️

Bridge to postgres:
`./cloud-sql-proxy instance_name`

Deploy:
`gcloud app deploy`
