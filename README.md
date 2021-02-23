# minor_django_project

### Node: #### Need to wait after registration for a while to recieve confirmation/activation message to your google email


## Step 1
- Install repository
#### git clone git@github.com:Caesark1/minor_django_project.git 
or 
#### git clone https://github.com/Caesark1/minor_django_project.git 

## Step 2
- Create images and container with command: 
#### docker-compose up -d --build

## Step 3
- makemigrations
#### docker-compose exec web python manage.py makemigrations

- migrate
#### docker-compose exec web python manage.py migrate

## Step 4
- Create superuser
#### docker-compose exec web python manage.py createsuperuser
