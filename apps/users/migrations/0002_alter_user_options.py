# Generated by Django 5.1 on 2024-09-09 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('users', 'Modulo de usuarios'), ('tipos', 'Modulo de Tipos '), ('publicaciones', 'Modulo de Publicaciones '), ('extras', 'Modulo Extras ')), 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
