# Generated by Django 3.2.5 on 2022-12-24 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('profile_pic', models.ImageField(blank=True, upload_to='userprofile/')),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('profile_updated', models.DateTimeField(auto_now=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superadmin', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
