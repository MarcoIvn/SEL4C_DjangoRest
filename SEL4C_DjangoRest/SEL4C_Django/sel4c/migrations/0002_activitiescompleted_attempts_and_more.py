
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sel4c', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitiescompleted',
            name='attempts',
            field=models.SmallIntegerField(default=3),
        ),
        migrations.AddField(
            model_name='activitiescompleted',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
