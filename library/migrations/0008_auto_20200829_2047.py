# Generated by Django 3.0.3 on 2020-08-29 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_auto_20200828_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='address',
            field=models.TextField(default='DEFAULT VALUE'),
        ),
        migrations.AlterField(
            model_name='books',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Genres'),
        ),
    ]
