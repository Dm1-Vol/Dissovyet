from django.db import models

# Create your models here.
from django.db import models


class Defence(models.Model):
    TYPE_CHOICES = [
        ('candidate', 'Кандидатская'),
        ('doctoral', 'Докторская'),
    ]

    STATUS_CHOICES = [
        ('scheduled', 'Назначена'),
        ('defended', 'Защищена'),
    ]

    title = models.CharField('Название темы', max_length=300)
    defence_type = models.CharField('Тип', max_length=20, choices=TYPE_CHOICES)
    defence_date = models.DateField('Дата защиты')
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='scheduled')
    author = models.CharField('Автор диссертации', max_length=150)

    def __str__(self):
        return f"{self.author} — {self.title[:50]}"

    class Meta:
        verbose_name = 'Защита'
        verbose_name_plural = 'Защиты'
        ordering = ['-defence_date']