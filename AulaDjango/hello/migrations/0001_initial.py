# Generated by Django 3.2.6 on 2021-08-03 03:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='filme')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Capa')),
            ],
        ),
    ]
