# Generated by Django 3.2.9 on 2021-12-06 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date_of_post',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
