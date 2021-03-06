# Generated by Django 2.0.2 on 2019-09-30 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20190930_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='pub_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='summary',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
