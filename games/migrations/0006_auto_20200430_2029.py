# Generated by Django 3.0.5 on 2020-04-30 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_auto_20200430_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='icon_url',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='logo_url',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.TextField(),
        ),
    ]
