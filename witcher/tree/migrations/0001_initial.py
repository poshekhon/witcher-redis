# Generated by Django 3.0.3 on 2020-03-06 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100)),
                ('parent_id', models.IntegerField()),
            ],
        ),
    ]
