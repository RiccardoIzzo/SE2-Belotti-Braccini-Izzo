# Generated by Django 4.0 on 2021-12-26 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SteeringInitiative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.FileField(upload_to='files/')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop_type', models.CharField(max_length=100)),
                ('qty_sown', models.IntegerField()),
                ('sown_date', models.DateField()),
                ('qty_harvested', models.IntegerField()),
                ('harvested_date', models.DateField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='HelpRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver_id', models.IntegerField()),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('sender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('score', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='DailyPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('farmer_user_id', models.IntegerField()),
                ('annotation', models.TextField()),
                ('agronomist_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop_type', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.user')),
            ],
        ),
    ]
