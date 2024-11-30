from django.db import models
from django.contrib.auth.models import User

class Workspace(models.Model):
    STATUS_CHOICES = [
        ('available', 'Доступно'),
        ('occupied', 'Занято'),
    ]
    id = models.IntegerField(primary_key=True)
    number = models.IntegerField(primary_key=True)
    description = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='available',
        verbose_name='статус'
    )


class Booking(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    start_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Время начала'
    )
    end_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Время конца'
    )