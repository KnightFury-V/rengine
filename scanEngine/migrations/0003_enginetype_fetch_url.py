# Generated by Django 3.0.7 on 2020-07-06 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanEngine', '0002_remove_enginetype_param_discovery'),
    ]

    operations = [
        migrations.AddField(
            model_name='enginetype',
            name='fetch_url',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
