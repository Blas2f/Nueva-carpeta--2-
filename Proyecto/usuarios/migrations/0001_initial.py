# Generated by Django 4.1.2 on 2024-07-01 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_cat', models.CharField(max_length=3)),
                ('nombre_cat', models.CharField(max_length=50)),
            ],
        ),
    ]
