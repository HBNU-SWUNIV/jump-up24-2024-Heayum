# Generated by Django 5.0.6 on 2024-05-15 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hyeeum', '0003_alter_book_library_id_alter_library_user_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'get_latest_by': 'id'},
        ),
    ]