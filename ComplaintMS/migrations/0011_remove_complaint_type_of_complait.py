# Generated by Django 3.2.2 on 2024-11-28 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ComplaintMS', '0010_auto_20241128_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='Type_of_complaint',
        ),
    ]