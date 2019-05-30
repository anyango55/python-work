from django.db import models

# Create your models here.
class Student(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	date_of_birth=models.DataField(max_length=20)
	registration_no=models.CharField(max_length=15)
	place_of_residence=models.CharField(max_length=50)
	phone_number=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)
	guardian_phone=models.CharField(max_length=50)
	id_number=models.IntegerField(max_length=8)
	date_joined=models.IntegerField(max_length=20)

class Teacher(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	date_of_birth=models.DataField()
	registration_no=models.CharField(max_length=20)
	place_of_residence=models.CharField(max_length=50)
	phone_number=models.CharField(max_length=50)
	email=models.EmailField()
	id_number=models.IntegerField(max_length=8)
	


