# Generated by Django 4.0.2 on 2022-03-14 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_kid_kid_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kid',
            name='parent_email_address',
            field=models.CharField(max_length=100),
        ),
    ]