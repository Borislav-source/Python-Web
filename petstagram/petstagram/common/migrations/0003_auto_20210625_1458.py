# Generated by Django 3.2.3 on 2021-06-25 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
        ('common', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.pet'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]