# Generated by Django 3.2 on 2021-05-15 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='pics')),
                ('contact', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='flats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('img', models.ImageField(upload_to='pics')),
                ('img1', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('img3', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('sqr_ft', models.IntegerField()),
                ('bhk', models.IntegerField()),
                ('est_year', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('owner_fullname', models.CharField(max_length=50)),
                ('owner_email', models.EmailField(max_length=250)),
                ('owner_contact', models.CharField(max_length=10)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.city')),
            ],
        ),
    ]
