# Generated by Django 4.1.5 on 2023-02-02 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samapp', '0015_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetailsmodel',
            name='uid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]