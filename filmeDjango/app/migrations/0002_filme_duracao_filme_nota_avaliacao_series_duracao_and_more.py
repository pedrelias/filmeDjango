# Generated by Django 4.2.5 on 2023-09-26 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='duracao',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filme',
            name='nota_avaliacao',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='duracao',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='filme',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.genero'),
        ),
    ]
