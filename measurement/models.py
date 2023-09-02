from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor,
                               on_delete=models.CASCADE,
                               related_name='measurements'
                               )
    temperature = models.DecimalField(max_digits=4, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
