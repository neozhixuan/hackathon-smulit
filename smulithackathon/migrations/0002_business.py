# Generated by Django 3.2.3 on 2021-08-14 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smulithackathon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('businesstype', models.CharField(blank=True, max_length=50, null=True)),
                ('employees', models.IntegerField(blank=True, null=True)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('profit', models.IntegerField(blank=True, null=True)),
                ('encryption', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]