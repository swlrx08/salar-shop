# Generated by Django 5.0.6 on 2024-07-03 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_cartorderitem_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='mobile_num',
            field=models.CharField(max_length=11, null=True),
        ),
    ]