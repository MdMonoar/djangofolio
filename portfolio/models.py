from django.db import models

# Create your models here.
class about(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    email  = models.EmailField()
    phone = models.CharField(max_length=20)
    nationality = models.CharField(max_length=255)

class Education(models.Model):
    edu_id = models.AutoField(primary_key=True)
    university_name = models.CharField(max_length=255)
    is_passed = models.BooleanField()
    passing_year = models.CharField(max_length=255, blank=True)
    # currently_studying = models.CharField(max_length=255, blank=True) # this will be derived

class Experience(models.Model):
    exp_id = models.AutoField(primary_key=True)
    position_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    starting_date = models.CharField(max_length=255)
    ending_date = models.CharField(max_length=255, blank=True)
    # currently_working = models.CharField(max_length=255, blank=True) # this will be derived

class Projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_title = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255, blank=True)
    completing_date = models.CharField(max_length=255, blank=True)
    # ongoing = models.BooleanField() # this will be derived from completing_date

