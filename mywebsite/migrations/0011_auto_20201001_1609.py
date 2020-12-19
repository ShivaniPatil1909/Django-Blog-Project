# Generated by Django 3.1.1 on 2020-10-01 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0010_myblog_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='myblog',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='myblog',
            name='snippet',
            field=models.CharField(max_length=255),
        ),
    ]