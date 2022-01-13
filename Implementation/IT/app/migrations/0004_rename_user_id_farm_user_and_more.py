# Generated by Django 4.0 on 2021-12-30 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0002_alter_user_district'),
        ('app', '0003_delete_dailyplan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='farm',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='production',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='crop',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='helprequest',
            name='receiver_id',
        ),
        migrations.RemoveField(
            model_name='helprequest',
            name='sender_id',
        ),
        migrations.AddField(
            model_name='crop',
            name='farm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.farm'),
        ),
        migrations.AddField(
            model_name='farm',
            name='visit_ctr',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='helprequest',
            name='receiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='receiver', to='userApp.user'),
        ),
        migrations.AddField(
            model_name='helprequest',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='userApp.user'),
        ),
    ]