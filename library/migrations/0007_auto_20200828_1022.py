# Generated by Django 3.0.3 on 2020-08-28 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20200826_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Genres'),
        ),
    ]
