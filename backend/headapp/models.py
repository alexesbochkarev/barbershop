from django.db import models
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField


class Feedback(models.Model):
    """
    Модель обратной связи
    """
    class Status(models.TextChoices):
     # Actual value ↓      # ↓ Displayed on Django Admin  
        CHECKED   = 'Checked', _('Не обработано')
        ALLOWED   = 'Allowed', _('Принято')
        REJECTED  = 'Rejected', _('Отклонено')
    name  = models.CharField('Имя', max_length=255)
    phone = PhoneNumberField('Номер телефона')
    date  = models.DateField('Желаемая дата записи')
    time  = models.TimeField('Желаемое время записи')
    actual_time = models.DateTimeField('Фактическое время записи', null=True, blank=True)
    time_create = models.DateTimeField('Дата отправки', auto_now_add=True)
    ip_address  = models.GenericIPAddressField('IP отправителя',  blank=True, null=True)
    status      = models.CharField('Статус', max_length=10, choices=Status.choices, default='Checked',)

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ['-time_create']
        db_table = 'app_feedback'

    def __str__(self):
        return f'Вам письмо от {self.name} | {self.phone}'