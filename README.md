# Ex02 Django ORM Web Application
## Date:13/09/2025 

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).




## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py
from django.db import models
from django.contrib import admin
class Car_DB(models.Model):
	car_name=models.CharField(max_length=20)
	chass_no=models.IntegerField(primary_key=True)	
	gear_box=models.CharField(max_length=20)
	model_name=models.CharField(max_length=30)
class Car_DBAdmin(admin.ModelAdmin):
	list_display=["car_name","chass_no","gear_box","model_name"]
admin.py
from django.contrib import admin
from .models import Car_DB,Car_DBAdmin
admin.site.register(Car_DB,Car_DBAdmin)

```


## OUTPUT
![alt text](<Screenshot 2025-09-13 131752.png>)



## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
