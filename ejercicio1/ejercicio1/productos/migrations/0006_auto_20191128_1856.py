# Generated by Django 2.2.7 on 2019-11-28 17:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_auto_20191128_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
