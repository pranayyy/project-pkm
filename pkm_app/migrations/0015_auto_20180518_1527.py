# Generated by Django 2.0.3 on 2018-05-18 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkm_app', '0014_auto_20180516_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildkb',
            name='keywords',
            field=models.TextField(blank=True, null=True),
        ),
    ]
