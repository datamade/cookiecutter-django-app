# Generated by Django 5.1.2 on 2024-10-10 15:14

from django.db import migrations
from django.core.management import call_command


def create_content(*args, **kwargs):
    call_command("initialize_database")


def destroy_content(*args, **kwargs):
    call_command("initialize_database", flush_only=True)


class Migration(migrations.Migration):
    dependencies = [
        ("{{ cookiecutter.module_name }}", "0002_examplemodel_examplemodeldetailpage"),
        ("wagtailsearch", "0006_customise_indexentry"),
        ("wagtailredirects", "0001_initial"),
        ("wagtailforms", "0001_initial"),
    ]

    operations = [migrations.RunPython(create_content, destroy_content)]
