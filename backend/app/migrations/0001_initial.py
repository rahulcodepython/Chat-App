# Generated by Django 4.2 on 2023-05-06 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_message', models.CharField(max_length=10000)),
                ('chat_time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
