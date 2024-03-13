from django.db import models


class Banner(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title
    

class Service(models.Model):
    name = models.CharField(max_length=255)
    body = models.TextField()
    icon = models.FileField(upload_to='service/')
    
    def __str__(self):
        return self.name
    

class AboutUs(models.Model):
    body = models.TextField()

    def __str__(self):
        return self.body
    

class Price(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    body = models.TextField()


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=255)
    body = models.TextField()
    is_show = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
