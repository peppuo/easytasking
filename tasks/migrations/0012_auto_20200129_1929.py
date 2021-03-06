# Generated by Django 2.2.8 on 2020-01-29 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0011_auto_20200129_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='tsk_category',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='tasks.Category'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='tsk_importance',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='tasks.Importance'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='tsk_status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tasks.Status'),
        ),
    ]
