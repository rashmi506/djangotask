from django.db import models


class clientss(models.Model):
    client_name = models.CharField(max_length=10)
    lastname = models.CharField(max_length=20)
    client_id = models.IntegerField()

    def __str__(self):
        return self.client_name
