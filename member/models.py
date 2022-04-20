from django.db import models

# Create your models here.
class Member(models.Model):
    company_name = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='profile_picture')
    company_info = models.TextField()
    address = models.TextField()
    contact_number = models.PositiveBigIntegerField()
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.company_name