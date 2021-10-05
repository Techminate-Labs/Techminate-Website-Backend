# Generated by Django 3.2.7 on 2021-10-04 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0004_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('bounty', models.CharField(max_length=100)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tasks', to='apis.jobs')),
            ],
            options={
                'verbose_name_plural': 'Tasks',
            },
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
