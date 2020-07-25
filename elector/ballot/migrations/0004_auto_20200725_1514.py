# Generated by Django 3.0.8 on 2020-07-25 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ballot', '0003_vote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voter_id', models.CharField(max_length=250)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('ballot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ballot.Ballot')),
            ],
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]