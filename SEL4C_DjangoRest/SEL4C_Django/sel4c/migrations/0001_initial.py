# Generated by Django 4.2.4 on 2023-10-20 18:47

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_num', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)], unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Entrepreneur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=25, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('degree', models.CharField(max_length=255)),
                ('institution', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('No binario', 'No binario'), ('Prefiero no decirlo', 'Prefiero no decirlo')], max_length=255)),
                ('age', models.IntegerField()),
                ('country', models.CharField(max_length=255)),
                ('studyField', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Entrepreneurs',
                'verbose_name_plural': 'Entrepreneurs',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_num', models.IntegerField(default=0)),
                ('description', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files/')),
                ('filetype', models.CharField(max_length=255)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sel4c.activity')),
                ('entrepreneur', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='sel4c.entrepreneur')),
            ],
        ),
        migrations.CreateModel(
            name='EntrepreneurProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result1', models.DecimalField(decimal_places=2, max_digits=5)),
                ('result2', models.DecimalField(decimal_places=2, max_digits=5)),
                ('result3', models.DecimalField(decimal_places=2, max_digits=5)),
                ('result4', models.DecimalField(decimal_places=2, max_digits=5)),
                ('result5', models.DecimalField(decimal_places=2, max_digits=5)),
                ('result6', models.DecimalField(decimal_places=2, max_digits=5)),
                ('result7', models.DecimalField(decimal_places=2, max_digits=5)),
                ('result8', models.DecimalField(decimal_places=2, max_digits=5)),
                ('result9', models.DecimalField(decimal_places=2, max_digits=5)),
                ('result10', models.DecimalField(decimal_places=2, max_digits=5)),
                ('result11', models.DecimalField(decimal_places=2, max_digits=5)),
                ('result12', models.DecimalField(decimal_places=2, max_digits=5)),
                ('result13', models.DecimalField(decimal_places=2, max_digits=5)),
                ('result14', models.DecimalField(decimal_places=2, max_digits=5)),
                ('result15', models.DecimalField(decimal_places=2, max_digits=5)),
                ('result16', models.DecimalField(decimal_places=2, max_digits=5)),
                ('result17', models.DecimalField(decimal_places=2, max_digits=5)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sel4c.activity')),
                ('entrepreneur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sel4c.entrepreneur')),
            ],
        ),
        migrations.CreateModel(
            name='EntrepreneurEcomplexity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result1', models.DecimalField(decimal_places=2, max_digits=5)),
                ('result2', models.DecimalField(decimal_places=2, max_digits=5)),
                ('result3', models.DecimalField(decimal_places=2, max_digits=5)),
                ('result4', models.DecimalField(decimal_places=2, max_digits=5)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sel4c.activity')),
                ('entrepreneur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sel4c.entrepreneur')),
            ],
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_staff', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.IntegerField(default=0)),
                ('activity', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='sel4c.activity')),
                ('entrepreneur', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='sel4c.entrepreneur')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sel4c.question')),
            ],
            options={
                'unique_together': {('question', 'entrepreneur', 'activity')},
            },
        ),
        migrations.CreateModel(
            name='ActivitiesCompleted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempts', models.SmallIntegerField(default=5)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sel4c.activity')),
                ('entrepreneur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sel4c.entrepreneur')),
            ],
            options={
                'verbose_name': 'Activities Completed',
                'verbose_name_plural': 'Activities Completed',
                'unique_together': {('activity', 'entrepreneur')},
            },
        ),
    ]
