# Generated by Django 3.0.3 on 2020-02-26 18:59

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Forbidden_Words',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forbidden_word', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=100)),
                ('post_image', models.ImageField(default='default.png', null=True, upload_to='')),
                ('post_text', models.CharField(max_length=900, null=True)),
                ('post_date', models.DateTimeField(default=datetime.datetime(2020, 2, 26, 18, 59, 43, 492077, tzinfo=utc))),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='djangoApp.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_email', models.CharField(max_length=100)),
                ('user_pass', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=100)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='djangoApp.Categories')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='djangoApp.Posts')),
            ],
        ),
        migrations.AddField(
            model_name='posts',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='djangoApp.Users'),
        ),
        migrations.CreateModel(
            name='Post_Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='djangoApp.Posts')),
                ('tag_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='djangoApp.Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Post_Likes_Dislikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='djangoApp.Posts')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=400)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 2, 26, 18, 59, 43, 492758, tzinfo=utc))),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='djangoApp.Posts')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='djangoApp.Users')),
            ],
        ),
    ]