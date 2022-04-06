# Generated by Django 4.0.3 on 2022-03-23 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_and_comments', '0003_alter_news_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(to='news_and_comments.tags'),
        ),
    ]