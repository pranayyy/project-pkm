# Generated by Django 2.0.3 on 2018-05-28 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkm_app', '0015_auto_20180518_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildkb',
            name='title',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='setupuser',
            name='your_job_level',
            field=models.CharField(choices=[('L1', 'Level 1'), ('L2', 'Level 2'), ('L3', 'Level 3'), ('L4', 'Level 4'), ('Newly Joined', 'Newly joined')], max_length=13),
        ),
    ]
