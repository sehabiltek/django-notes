# Generated by Django 2.0.5 on 2018-05-19 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hello_uptime', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitor',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monitors', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='url',
            field=models.URLField(verbose_name='URL'),
        ),
        migrations.AlterUniqueTogether(
            name='monitor',
            unique_together={('user', 'url')},
        ),
    ]