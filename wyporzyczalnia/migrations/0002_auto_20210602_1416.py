# Generated by Django 3.2.3 on 2021-06-02 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wyporzyczalnia', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='relise',
            new_name='release',
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='okładki'),
        ),
    ]
