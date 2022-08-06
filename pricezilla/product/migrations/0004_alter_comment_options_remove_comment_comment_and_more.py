# Generated by Django 4.0.6 on 2022-08-06 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.TextField(default='naddsn', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default='sasas', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='asds', max_length=80),
            preserve_default=False,
        ),
    ]
