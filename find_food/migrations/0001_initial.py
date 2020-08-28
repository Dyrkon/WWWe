# Generated by Django 3.1 on 2020-08-19 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.FloatField()),
                ('link', models.TextField()),
                ('ingredients', models.TextField()),
                ('u_ingredients', models.TextField()),
            ],
        ),
    ]