# Generated by Django 2.0.7 on 2018-08-20 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('keystate', '0007_auto_20180820_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempKeys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keytag', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='keyhistory',
            name='keytag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='keystate.Key'),
        ),
    ]
