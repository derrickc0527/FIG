# Generated by Django 2.0.2 on 2018-10-21 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20180513_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='dealStatus',
            field=models.CharField(choices=[('CONTRACT REQUESTED', 'contract requested'), ('CONTRACT OUT', 'contract out'), ('SIGNED CONTRACT', 'signed contract'), ('FUNDED', 'funded')], default='CONTRACT REQUESTED', max_length=15),
        ),
    ]
