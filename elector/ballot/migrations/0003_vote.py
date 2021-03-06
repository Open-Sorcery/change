# Generated by Django 3.0.8 on 2020-07-25 14:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ballot', '0002_auto_20200717_1755'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voter_id', models.CharField(max_length=250)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('ballot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ballot.Ballot')),
            ],
        ),
    ]
