# Generated by Django 2.2.6 on 2019-10-29 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20191029_1355'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dynamic',
            options={'ordering': ('month',), 'verbose_name': 'Динамика показателей', 'verbose_name_plural': 'Динамика показателей'},
        ),
    ]
