# Generated by Django 4.2.2 on 2023-08-10 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nextapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default=2, upload_to=''),
            preserve_default=False,
        ),
    ]
