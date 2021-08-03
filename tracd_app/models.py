from django.db import models
import datetime

class Book(models.Model):
	CATEGORY=(

			('Anna Nagar','Anna Nagar'),
			('Alanthur','Alanthur'),
			('Parrys Corner','Parrys Corner'),
			('Porur','Porur'),
			('Vadapalani','Vadapalani'),
			('Koyembedu','Koyembedu'),
			
		)

	
	Name=models.CharField(max_length=100, null=True)
	No_of_tickets=models.IntegerField(null=True)
	To=models.CharField(max_length=100, null=True, choices=CATEGORY)
	From=models.CharField(max_length=100, null=True, choices=CATEGORY)
	Time_of_arrival=models.TimeField(auto_now=False, auto_now_add=False)
	date = models.DateField(("Date"), default=datetime.date.today)
	Main_Img = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.Name


# Create your models here.
class Schedule(models.Model):
	CATEGORY=(

			('Anna Nagar','Anna Nagar'),
			('Alanthur','Alanthur'),
			('Parrys Corner','Parrys Corner'),
			('Porur','Porur'),
			('Vadapalani','Vadapalani'),
			('Koyembedu','Koyembedu'),
			
		)

	CATEGORY2=(

		('Arriving...','Arriving...'),
		('Departed Already','Departed Already'),
		('Cancelled','Cancelled'),
		('Late','Late'),
		)
	date=models.DateTimeField(auto_now_add=True, null=True)
	Train_No=models.CharField(max_length=100, null=True)
	To=models.CharField(max_length=100, null=True, choices=CATEGORY)
	From=models.CharField(max_length=100, null=True, choices=CATEGORY)
	Train_fare=models.FloatField(null=True)
	Train_Status=models.CharField(max_length=100, null=True, choices=CATEGORY2)
	Time_of_arrival=models.TimeField(auto_now=False, auto_now_add=False)
	
	

	def __str__(self):
		return self.Train_No



