# Generated by Django 2.2.1 on 2019-05-31 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minerals', '0003_auto_20190531_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mineral',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
