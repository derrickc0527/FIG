# Generated by Django 2.0.2 on 2018-05-05 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='description',
        ),
        migrations.RemoveField(
            model_name='products',
            name='price',
        ),
        migrations.RemoveField(
            model_name='products',
            name='quantity',
        ),
        migrations.AddField(
            model_name='products',
            name='caller',
            field=models.CharField(max_length=26, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='dealName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='dealStatus',
            field=models.CharField(choices=[('CONTRACT OUT', 'contract out'), ('SIGNED CONTRACT', 'signed contract'), ('FUNDED', 'funded')], default='CONTRACT OUT', max_length=15),
        ),
    ]
