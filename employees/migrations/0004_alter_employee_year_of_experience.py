# Generated by Django 3.2.12 on 2023-05-22 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_auto_20230522_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='year_of_experience',
            field=models.IntegerField(null=True),
        ),
    ]