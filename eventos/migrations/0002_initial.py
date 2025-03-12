# Generated by Django 4.2.20 on 2025-03-12 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eventos', '0001_initial'),
        ('resultados', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='resultado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='eventos_asociados', to='resultados.resultado'),
        ),
    ]
