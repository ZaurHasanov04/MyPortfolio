# Generated by Django 3.2.5 on 2021-07-17 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_alter_skill_icons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='icons',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
