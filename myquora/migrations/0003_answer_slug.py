# Generated by Django 3.1.4 on 2020-12-11 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myquora', '0002_auto_20201211_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='slug',
            field=models.SlugField(allow_unicode=True, default=None, max_length=150, unique=True, verbose_name=' نامک'),
            preserve_default=False,
        ),
    ]