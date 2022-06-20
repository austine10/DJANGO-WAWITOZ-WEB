from django.db import models


# Create your models here.
class JobApplicant(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    cv = models.ImageField()
    position = models.CharField(max_length=100)
    age = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.firstname


class FutureJobsApplicant(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    cv = models.ImageField()
    position = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=30)

    def __str__(self):
        return self.firstname

class Job(models.Model):
    Job_Title = models.CharField(max_length=30)
    Job_Salary = models.CharField(max_length=30)
    Job_Description = models.CharField(max_length=30)

    def __str__(self):
        return self.Job_Title

