# Generated by Django 2.2.15 on 2020-09-04 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipl_analysis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveries',
            name='ball',
        ),
        migrations.RemoveField(
            model_name='deliveries',
            name='bye_runs',
        ),
        migrations.RemoveField(
            model_name='deliveries',
            name='dismissal_kind',
        ),
        migrations.RemoveField(
            model_name='deliveries',
            name='extra_runs',
        ),
        migrations.RemoveField(
            model_name='deliveries',
            name='fielder',
        ),
        migrations.RemoveField(
            model_name='deliveries',
            name='is_super_over',
        ),
        migrations.RemoveField(
            model_name='deliveries',
            name='legbye_runs',
        ),
        migrations.RemoveField(
            model_name='deliveries',
            name='noball_runs',
        ),
        migrations.RemoveField(
            model_name='deliveries',
            name='non_striker',
        ),
        migrations.RemoveField(
            model_name='deliveries',
            name='over',
        ),
        migrations.RemoveField(
            model_name='deliveries',
            name='penalty_runs',
        ),
        migrations.RemoveField(
            model_name='deliveries',
            name='player_dismissed',
        ),
        migrations.RemoveField(
            model_name='deliveries',
            name='wide_runs',
        ),
    ]
