# Generated by Django 3.1.5 on 2021-04-13 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0010_org_primarily_concerned_with_brain_area'),
    ]

    operations = [
        migrations.RenameField(
            model_name='org',
            old_name='locations',
            new_name='all_locations',
        ),
        migrations.RenameField(
            model_name='org',
            old_name='country_hq',
            new_name='country_HQ',
        ),
    ]
