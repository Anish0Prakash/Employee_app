from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo_upload = models.ImageField(upload_to="images")
    designation = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name