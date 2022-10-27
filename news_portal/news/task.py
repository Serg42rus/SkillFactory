from celery import shared_task
import time
from .models import *
from datetime import datetime
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


@shared_task()
def news_sender():
    for category in Category.objects.all():
        news_from_each_category = []
        week_number_last = datetime.now().isocalendar()[1] - 1
        for news in Post.objects.filter(post_category=category.id, creation_date__week=week_number_last).values(
                                                                                    'pk',
                                                                                    'title',
                                                                                    'creation_date',
                                                                                    'post_category__category_name'):

            date_format = news.get('creation_date').strftime("%m/%d/%Y")
            new = (f' http://127.0.0.1:8000/news/{news.get("pk")}, {news.get("title")}, '
                   f'Категория: {news.get("post_category__category_name")}, Дата создания: {date_format}')

            news_from_each_category.append(new)

        subscribers = category.subscriber.all()

        for subscriber in subscribers:
            html_content = render_to_string(
                'subscription_letter_weekly.html', {'user': subscriber,
                                                    'text': news_from_each_category,
                                                    'category_name': category.category_name,
                                                    'week_number_last': week_number_last})

            msg = EmailMultiAlternatives(
                subject=f'Здравствуйте, {subscriber.username}, новые публикации за неделю!',
                from_email='serg42rus@yugs.ru',
                to=[subscriber.email]
            )

            if news_from_each_category:
                msg.attach_alternative(html_content, 'week_email/html')

                msg.send()