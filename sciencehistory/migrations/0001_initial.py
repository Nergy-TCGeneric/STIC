# Generated by Django 2.1.7 on 2019-07-18 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('rank', models.PositiveIntegerField(default=0)),
                ('created_date', models.DateTimeField(verbose_name='Created time')),
            ],
        ),
    ]