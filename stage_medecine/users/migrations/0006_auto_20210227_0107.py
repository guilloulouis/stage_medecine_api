# Generated by Django 3.1.6 on 2021-02-27 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stages', '0005_auto_20210227_0107'),
        ('users', '0005_auto_20210220_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='code',
        ),
        migrations.AlterField(
            model_name='student',
            name='stages_done',
            field=models.ManyToManyField(blank=True, to='stages.StageDone'),
        ),
        migrations.DeleteModel(
            name='ConnectCode',
        ),
    ]
