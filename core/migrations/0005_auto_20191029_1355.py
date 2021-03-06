# Generated by Django 2.2.6 on 2019-10-29 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20191028_2346'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dynamic',
            options={'ordering': ('month',), 'verbose_name': 'Динамика показателей'},
        ),
        migrations.AlterModelOptions(
            name='indicator',
            options={'ordering': ('group',), 'verbose_name': 'Показатель', 'verbose_name_plural': 'Показатели'},
        ),
        migrations.AlterModelOptions(
            name='office',
            options={'ordering': ('id',), 'verbose_name': 'Офис', 'verbose_name_plural': 'Офисы'},
        ),
        migrations.AlterField(
            model_name='dynamic',
            name='indicator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dynamic', to='core.Indicator', verbose_name='Показатель'),
        ),
        migrations.AlterField(
            model_name='dynamic',
            name='month',
            field=models.DateField(verbose_name='Месяц'),
        ),
        migrations.AlterField(
            model_name='dynamic',
            name='office',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dynamic', to='core.Office', verbose_name='Офис'),
        ),
        migrations.AlterField(
            model_name='dynamic',
            name='value',
            field=models.BigIntegerField(verbose_name='Значение'),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='group',
            field=models.CharField(max_length=200, verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Показатель'),
        ),
        migrations.AlterField(
            model_name='office',
            name='city',
            field=models.CharField(max_length=200, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='office',
            name='department',
            field=models.CharField(max_length=200, verbose_name='ТО'),
        ),
        migrations.AlterField(
            model_name='office',
            name='id',
            field=models.SmallIntegerField(primary_key=True, serialize=False, verbose_name='Офис'),
        ),
        migrations.AlterField(
            model_name='office',
            name='slug',
            field=models.SlugField(default='', max_length=200, verbose_name='URL'),
        ),
    ]
