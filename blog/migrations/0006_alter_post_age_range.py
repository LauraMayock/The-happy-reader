# Generated by Django 3.2.15 on 2022-11-14 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='age_range',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='age', to='blog.age_range'),
        ),
    ]
