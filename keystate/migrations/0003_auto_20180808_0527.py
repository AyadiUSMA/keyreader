# Generated by Django 2.0.7 on 2018-08-08 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('keystate', '0002_auto_20180808_0434'),
    ]

    operations = [
        migrations.AddField(
            model_name='key',
            name='key_categ',
            field=models.CharField(default='white', max_length=50),
        ),
        migrations.AlterField(
            model_name='keyhistory',
            name='keytag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='keystate.Key'),
        ),
        migrations.AlterField(
            model_name='keyhistory',
            name='state_checkout',
            field=models.BooleanField(default=True),
        ),
    ]
