from django.db import models


class Vacancy(models.Model):
    CHART_CHOICES = [
        ('FD', 'Full day'),
        ('PT', 'Part-time'),
        ('PJ', 'Project'),
        ('FD or PT', 'May be Full day or Part-time'),
    ]
    title = models.CharField(max_length=50)
    description = models.TextField()
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()
    min_experience = models.IntegerField()
    max_experience = models.IntegerField()
    chart = models.CharField(max_length=40, choices=CHART_CHOICES)
    duties = models.TextField()
    requirements = models.TextField()
    conditions = models.TextField()
    online = models.BooleanField()
    available = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=True)





