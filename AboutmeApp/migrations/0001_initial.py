# Generated by Django 4.0.2 on 2022-02-20 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('contenido', models.CharField(max_length=250)),
                ('imagen', models.ImageField(upload_to='Aboutme')),
            ],
            options={
                'verbose_name': 'aboutme',
                'verbose_name_plural': 'aboutmes',
            },
        ),
    ]
