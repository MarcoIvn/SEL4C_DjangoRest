# Generated by Django 4.2.4 on 2023-10-13 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sel4c', '0003_remove_activitiescompleted_is_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitiescompleted',
            name='attempts',
            field=models.SmallIntegerField(default=1),
        ),
    ]