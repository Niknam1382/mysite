# Generated by Django 4.2.7 on 2023-11-11 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_alter_contact_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
