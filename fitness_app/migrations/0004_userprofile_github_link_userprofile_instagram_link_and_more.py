# Generated by Django 5.0 on 2024-02-07 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_app', '0003_rename_username_userregistrationform_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='github_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='instagram_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='twitter_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]