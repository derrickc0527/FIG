# Generated by Django 2.0.2 on 2018-05-13 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20180513_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='tranDate',
            field=models.DateField(null=True),
        ),
    ]