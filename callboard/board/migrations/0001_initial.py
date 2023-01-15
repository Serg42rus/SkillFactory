# Generated by Django 4.1.1 on 2022-12-19 12:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('CategoryType', models.CharField(choices=[('TANK', 'танк'), ('HILL', 'хиллы'), ('DD', 'ДД'), ('DILL', 'торговец'), ('GM', 'гилдмастер'), ('QUES', 'Квестгивер'), ('SMI', 'Кузнец'), ('SKIN', 'Кожевник'), ('WHIT', 'Зельевар'), ('WIZ', 'Мастер заклинаний')], max_length=4)),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratingAuthor', models.SmallIntegerField(default=0)),
                ('authorUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Respond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=128)),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('rating', models.SmallIntegerField(default=0)),
                ('respondAdvert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.advert')),
                ('respondAuthor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.author')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='advert',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.author'),
        ),
    ]