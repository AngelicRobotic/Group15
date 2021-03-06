# Generated by Django 3.1.7 on 2021-04-09 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20210409_0029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtask',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='subtask',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='subtask',
            name='id',
        ),
        migrations.RemoveField(
            model_name='subtask',
            name='task',
        ),
        migrations.RemoveField(
            model_name='subtask',
            name='time_estimate',
        ),
        migrations.AddField(
            model_name='subtask',
            name='empty_field',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='subtask',
            name='task_ptr',
            field=models.OneToOneField(auto_created=True, default=22, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.task'),
            preserve_default=False,
        ),
    ]
