# Generated by Django 2.0.7 on 2018-08-22 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('keystate', '0008_auto_20180820_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyhistory',
            name='keytag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='keystate.Key'),
        ),
    ]