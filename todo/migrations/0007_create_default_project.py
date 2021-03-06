# Generated by Django 3.1.1 on 2020-10-29 18:16

from django.db import migrations


def create_default_project(apps, schema_edition):
    Project = apps.get_model('todo', 'Project')
    def_project = Project(
        id_project="DEF",
        name="Projecto por defecto",
    )
    def_project.save()


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_project'),
    ]

    operations = [
        migrations.RunPython(create_default_project)
    ]
