from django.db import models
from django.core.exceptions import ValidationError
from datetime import date


class Defence(models.Model):
    TYPE_CHOICES = [
        ('candidate', 'Кандидатская'),
        ('doctoral', 'Докторская'),
    ]

    STATUS_CHOICES = [
        ('scheduled', 'Назначена'),
        ('defended', 'Защищена'),
        ('failed', 'Не защищена'),
    ]

    title = models.CharField('Название темы', max_length=300)
    defence_type = models.CharField('Тип', max_length=20, choices=TYPE_CHOICES)
    defence_date = models.DateField('Дата защиты')
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='scheduled')
    author = models.CharField('Автор диссертации', max_length=150)

    def __str__(self):
        return f"{self.author} — {self.title[:50]}"

    def clean(self):
        """Валидация дат в зависимости от статуса"""
        if self.status == 'defended' and self.defence_date > date.today():
            raise ValidationError('Дата защиты не может быть в будущем для уже защищённой диссертации')

        if self.status == 'failed' and self.defence_date > date.today():
            raise ValidationError('Дата защиты не может быть в будущем для диссертации, которая не защищена')

    class Meta:
        verbose_name = 'Защита'
        verbose_name_plural = 'Защиты'
        ordering = ['-defence_date']