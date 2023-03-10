# Generated by Django 4.1.5 on 2023-02-01 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0004_alter_street_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='street',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AddConstraint(
            model_name='street',
            constraint=models.UniqueConstraint(fields=('name', 'city'), name='name_city_constraint'),
        ),
    ]
