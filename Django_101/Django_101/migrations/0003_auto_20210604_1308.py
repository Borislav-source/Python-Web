# Generated by Django 3.2.3 on 2021-06-04 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Django_101', '0002_auto_20210527_1604'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='name',
            new_name='fname',
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='lname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
