For starting you should create a media folder, where you will store your images for meals/news.
=========================

**Project already have some default name for dishes** 

Let`s start configuration app. First of all you need to add your params in docker/env. Replace <> to what you want. 

* After that step let`s build our app! Write commands bellow in console.

* ````` docker compose build ````` 
* ````` docker compose run `````
  
So our app working!
Now let`s create a super user! Open new terminal
````` docker exec django -it `````
Why we should add **-it**? For creating super user which allow us to operate admin panel via creating interactive container terminal.

To create superuser type in interactive terminal **python manage.py createsuperuser**.
Now you can work in admin panel


