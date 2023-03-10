# Generated by Django 4.1.5 on 2023-02-01 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0002_alter_street_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='street',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city.city', to_field='name'),
        ),
    ]
