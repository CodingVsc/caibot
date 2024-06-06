from django.db import models


class Client(models.Model):
    account_number = models.CharField(max_length=100, verbose_name="Номер счета", unique=True)
    created_at = models.DateField(auto_now_add=True, verbose_name="дата добавления клиента/начала лицензии")
    date_to = models.DateField(verbose_name="дата окончания лицензии")

    def __str__(self):
        return self.account_number

    class Meta:
        db_table = 'client'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['created_at']


class Message(models.Model):
    message = models.CharField(max_length=100, verbose_name="Сообщение пользователям")

    def __str__(self):
        return self.message

    class Meta:
        db_table = 'message'
        verbose_name = 'Сообщение клиентам'
        verbose_name_plural = 'Сообщения клиентам'
