# Generated by Django 4.1.4 on 2022-12-19 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_feature_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='surname',
            field=models.CharField(default='Nkasi ', max_length=50),
        ),
    ]
