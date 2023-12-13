from django.db import models

class Contacts(models.Model):
    contact_name = models.CharField(max_length = 200)
    contact_email = models.CharField(max_length = 200)
    contact_notes = models.CharField(max_length=50)
    created_time = models.CharField(max_length=25)

    def __str__(self):
        return self.contact_name