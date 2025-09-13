from django.db import models
from django.contrib import admin
class Car_DB(models.Model):
	car_name=models.CharField(max_length=20)
	chass_no=models.IntegerField(primary_key=True)	
	gear_box=models.CharField(max_length=20)
	model_name=models.CharField(max_length=30)
class Car_DBAdmin(admin.ModelAdmin):
	list_display=["car_name","chass_no","gear_box","model_name"]

