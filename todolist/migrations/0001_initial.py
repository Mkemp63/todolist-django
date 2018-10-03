# Generated by Django 2.1.2 on 2018-10-03 14:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_title', models.CharField(default='Unnamed', max_length=200)),
                ('item_description', models.TextField(blank=True, max_length=200, null=True)),
                ('due', models.DateTimeField(blank=True, null=True)),
                ('done', models.BooleanField(default=False)),
                ('modified_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['due'],
            },
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_title', models.CharField(max_length=30)),
                ('list_priority', models.IntegerField()),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'TodoItem',
                'verbose_name_plural': 'TodoItems',
                'ordering': ['list_priority'],
            },
        ),
        migrations.AddField(
            model_name='todoitem',
            name='item_list',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.DO_NOTHING, related_name='items', to='todolist.TodoList'),
        ),
    ]
