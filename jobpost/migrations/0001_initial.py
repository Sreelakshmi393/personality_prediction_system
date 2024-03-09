# Generated by Django 3.2.12 on 2023-03-02 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hod',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('id_proof', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('department', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=150)),
                ('position', models.CharField(max_length=150)),
                ('gender', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='reg',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
            ],
        ),
    ]
