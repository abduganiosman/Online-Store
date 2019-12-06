# Generated by Django 2.2.6 on 2019-11-25 11:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('epay', '0002_item_currentbid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='biddings',
            field=models.CharField(blank=True, max_length=100000),
        ),
        migrations.AlterField(
            model_name='item',
            name='currentBid',
            field=models.CharField(blank=True, max_length=100000),
        ),
        migrations.AlterField(
            model_name='item',
            name='winner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]