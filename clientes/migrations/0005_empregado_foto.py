# Generated by Django 3.2.3 on 2021-05-31 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_auto_20210530_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='empregado',
            name='foto',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
