from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post
import smtplib


@receiver(post_save, sender=Post)
def notify_managers_post(sender, instance, created, **kwargs):
    if created:
        subject = f'Новая статья на News Portal - {instance.title_news} {instance.date_time_create.strftime("%d %m %Y")}'
    else:
        subject = f'Статья была изменена {instance.title_news} {instance.date_time_create.strftime("%d %m %Y")}'
    send = "serg42rus@yugs.ru"
    # your password = "your password"
    password = "5cqweYjVfiBBNPo2LyTZ"
    server = smtplib.SMTP("smtp.yandex.ru", 25)
    server.starttls()