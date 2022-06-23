# -*- coding: utf-8 -*-

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainees',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('names', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('username', models.CharField(max_length=100, null=True)),
                ('dob', models.DateField()),
                ('location', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'trainees',
            },
        ),
    ]
