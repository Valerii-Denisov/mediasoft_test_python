# Generated by Django 4.1.5 on 2023-02-02 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0006_alter_street_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='street',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city', to='city.city'),
        ),
    ]
