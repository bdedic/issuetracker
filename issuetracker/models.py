from django.db import models


# Create your models here.
class Issue(models.Model):
    STATUS = (
        ('Assigned', 'Assigned'),
        ('Closed', 'Closed'),
    )
    CATEGORY = (
        ('Bug', 'Bug'),
        ('Enhancements', 'Enhancements'),
        ('Documentation', 'Documentation')
    )
    submitter = models.CharField(max_length=30)
    solver = models.CharField(max_length=30, null=True, blank=True)
    description = models.CharField(max_length=500)
    status = models.CharField(max_length=8, choices=STATUS)
    category = models.CharField(max_length=13, choices=CATEGORY)
    opened = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description





