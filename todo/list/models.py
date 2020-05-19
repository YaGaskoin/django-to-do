from django.db import models

# Create your models here.


class Task(models.Model):
    PRIORITY_CHOICES = (('Высокий', 'Высокий'),
                        ('Средний', 'Средний'),
                        ('Низкий', 'Низкий'))
    STATUS_CHOICES = (('Ожидает выполнения', 'Ожидает выполнения'),
                      ('В процессе выполнения', 'В процессе выполнения'),
                      ('Выполнена', 'Выполнена'))
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(db_index=True, auto_now_add=True)
    deadline = models.DateTimeField(db_index=True)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Ожидает выполнения')

    class Meta:
        ordering = ('-created',)
