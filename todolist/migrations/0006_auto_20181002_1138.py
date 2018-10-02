# Generated by Django 2.1.2 on 2018-10-02 09:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_auto_20181002_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='due',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='modified_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]