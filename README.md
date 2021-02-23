# minor_django_project

## Node: 
### Need to wait after registration for a while to recieve confirmation/activation message to your google email

## Node2:
### This project didn't tested in windows, it can be working only on linux/mac. 

## Step 1
- Install repository
#### git clone git@github.com:Caesark1/minor_django_project.git 
or 
#### git clone https://github.com/Caesark1/minor_django_project.git 

## Step 2
#### cd minor_django_project

## Step 3
- Create images and container with command: 
#### docker-compose up -d --build

## Step 4
- makemigrations
#### docker-compose exec web python manage.py makemigrations

- migrate
#### docker-compose exec web python manage.py migrate

## Step 5
- Create superuser
#### docker-compose exec web python manage.py createsuperuser

And than go to the http://127.0.0.1:8000/
