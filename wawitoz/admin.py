from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.JobApplicant)
admin.site.register(models.FutureJobsApplicant)
admin.site.register(models.Job)

