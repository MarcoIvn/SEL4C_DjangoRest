# Generated by Django 4.2.4 on 2023-10-13 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sel4c', '0007_alter_activity_activity_num'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together={('question', 'entrepreneur', 'activity')},
        ),
    ]
