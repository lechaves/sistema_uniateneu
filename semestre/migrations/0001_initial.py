# Generated by Django 4.0.3 on 2022-03-24 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=5)),
                ('descricao', models.CharField(max_length=25)),
            ],
        ),
    ]
