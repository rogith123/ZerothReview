# Generated by Django 4.0.5 on 2022-06-05 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dr', '0002_remove_pat_ap_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='pat_ap',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
