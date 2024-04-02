
###
Ваши пути blog_api/home   blog_api/about



### 02.04.2024
1 Создание models class Posts
2 добавили  Meta class 
3 переопредилили __str__()
4 Миграция 
   4.1 makemigrations  после создания модели, создаёт файл
   4.2 migrate применить миграцию , тоесть выполнить SQL скрипт 

   python manage.py makemigrations
   python manage.py sqlmigrate blog_api 0001
   python manage.py migrate 
   passwd 1234 : admin
