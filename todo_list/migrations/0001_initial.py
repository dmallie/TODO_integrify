# Generated by Django 3.2.5 on 2022-12-25 12:14

import ckeditor.fields
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
            name='Calendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(default=1)),
                ('month', models.IntegerField(default=1)),
                ('year', models.IntegerField(default=2022)),
                ('week_day', models.IntegerField(default=1)),
                ('slug', models.SlugField(max_length=25, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_created_at', models.DateField(auto_now_add=True)),
                ('event_scheduled_to_begin', models.TimeField()),
                ('event_scheduled_to_end', models.TimeField()),
                ('event_description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('event_title', models.CharField(max_length=50)),
                ('calendar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_list.calendar')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
