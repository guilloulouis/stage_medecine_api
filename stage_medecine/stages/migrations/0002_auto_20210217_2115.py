# Generated by Django 3.1.6 on 2021-02-17 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stagedone',
            name='period',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stages.period'),
        ),
    ]
