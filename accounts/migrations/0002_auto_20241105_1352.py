# Generated by Django 5.1.3 on 2024-11-05 21:52

from django.db import migrations


def populate_role(apps, schemaeditor):
    entries = {
        "developer": "The person who actually works on issues",
        "scrum master": "The team's coach",
        "product owner": "Responsible for defining work and deliverables"
    }
    Role = apps.get_model("accounts", "role")
    for key, value in entries.items():
        role = Role(name=key, description=value)
        role.save()



class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
    ]
