# Generated by Django 3.2.7 on 2021-09-28 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0003_remove_messagebox_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagebox',
            name='message',
            field=models.CharField(max_length=100, null=True),
        ),
    ]