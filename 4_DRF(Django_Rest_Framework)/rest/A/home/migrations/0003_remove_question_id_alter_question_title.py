# Generated by Django 4.2.6 on 2023-12-13 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_question_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='id',
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]