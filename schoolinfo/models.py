from django.db import models

# Create your models here.

class Schooldata(models.Model):
	region = models.IntegerField(default=100)
	school_name = models.CharField(max_length=30,primary_key=True)
	email = models.EmailField(max_length=70,blank=False, null= False, unique= True)
	principal_name = models.CharField(max_length=30,null=False)
	phone_number = models.CharField(max_length=8,null=False)
	address = models.CharField(max_length=40)

class Bookdata(models.Model):
	title = models.CharField(max_length=30,primary_key=True)
	authorname = models.CharField(max_length=30, null=True, blank=True)
	date_of_publication = models.DateField(auto_now=False,null= True, blank=True)
	number_of_pages = models.IntegerField()

class Studentdata(models.Model):
	id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=30, null=False)
	last_name =  models.CharField(max_length=30, null=True, blank=True)
	email = models.EmailField(max_length=70,blank=False, null= False, unique= True)
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
	school = models.ForeignKey(Schooldata, on_delete=models.CASCADE)
	books = models.ForeignKey(Bookdata, on_delete=models.CASCADE,null = True, blank=True)
	add_date = models.DateTimeField(auto_now_add=True)
