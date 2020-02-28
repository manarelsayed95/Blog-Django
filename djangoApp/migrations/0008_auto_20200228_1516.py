# Generated by Django 3.0.3 on 2020-02-28 15:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djangoApp', '0007_auto_20200228_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 28, 15, 16, 36, 433615, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 28, 15, 16, 36, 432256, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='postrates',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
