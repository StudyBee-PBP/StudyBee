# Generated by Django 4.1.7 on 2023-04-20 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_bee', '0002_alter_transactionrecord_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('deadline', models.DateField()),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
