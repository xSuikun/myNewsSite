# Generated by Django 3.2.5 on 2021-09-04 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20210818_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='news.category', verbose_name='Категория'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано?'),
        ),
    ]