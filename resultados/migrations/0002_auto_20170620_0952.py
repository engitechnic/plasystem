# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-20 15:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resultados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcuerdoComercial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_contrato', models.IntegerField(choices=[(4, 'c.1) Contrato escrito'), (5, 'c.2) Contrato verbal')])),
                ('periodo', models.CharField(max_length=150, verbose_name='c.3.Periodo del contrato')),
                ('resultado_implementacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resultados.ResultadosImplementacion')),
            ],
            options={
                'verbose_name_plural': 'Acuerdo comerciales',
            },
        ),
        migrations.AlterModelOptions(
            name='digitador',
            options={'verbose_name': 'Digitador', 'verbose_name_plural': 'Digitadores'},
        ),
        migrations.RenameField(
            model_name='aumentadoingresos',
            old_name='valor',
            new_name='area_hombre_cosechada',
        ),
        migrations.RenameField(
            model_name='aumentadoproductividad',
            old_name='valor',
            new_name='area_hombre_cosechada',
        ),
        migrations.AddField(
            model_name='aumentadoingresos',
            name='area_hombre_sembrada',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aumentadoingresos',
            name='area_mujer_cosechada',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aumentadoingresos',
            name='area_mujer_sembrada',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aumentadoingresos',
            name='cantidad',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aumentadoingresos',
            name='cantidad_certificada',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aumentadoingresos',
            name='cantidad_hombres',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aumentadoingresos',
            name='cantidad_mujeres',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aumentadoingresos',
            name='precio_promedio',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aumentadoingresos',
            name='unidad_medida',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aumentadoproductividad',
            name='area_hombre_sembrada',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aumentadoproductividad',
            name='area_mujer_cosechada',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aumentadoproductividad',
            name='area_mujer_sembrada',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aumentadoproductividad',
            name='cantidad',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aumentadoproductividad',
            name='cantidad_certificada',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aumentadoproductividad',
            name='cantidad_hombres',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aumentadoproductividad',
            name='cantidad_mujeres',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aumentadoproductividad',
            name='precio_promedio',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aumentadoproductividad',
            name='unidad_medida',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='incrementoabastecimiento',
            name='cantidad_hombres',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='incrementoabastecimiento',
            name='cantidad_mujeres',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='desempenofinanciero',
            name='opciones',
            field=models.IntegerField(choices=[(1, 'Total Desempe\xf1o financiero'), (2, 'Balance General'), (3, 'Estado de resultado'), (4, 'P\xe9rdidas y ganancias')]),
        ),
        migrations.AlterField(
            model_name='facilitadores',
            name='opciones',
            field=models.IntegerField(choices=[(1, 'Total facilitadores'), (2, 'Desarrolladores de capacidades y ONG'), (3, 'Proveedores de servicios'), (4, 'Organizaciones del sector'), (5, 'Comunidad'), (6, 'Gobierno y regulaciones')]),
        ),
        migrations.AlterField(
            model_name='gestionfinanciera',
            name='opciones',
            field=models.IntegerField(choices=[(1, 'Total gesti\xf3n financiera'), (2, 'Gesti\xf3n financiera'), (3, 'Planificaci\xf3n financiera'), (4, 'Registro de informaci\xf3n y monitoreo')]),
        ),
        migrations.AlterField(
            model_name='gestioninterna',
            name='opciones',
            field=models.IntegerField(choices=[(1, 'Total Gestion interna'), (2, 'Gobernabilidad'), (3, 'Organizaci\xf3n interna'), (4, 'Planificaci\xf3n de negocios')]),
        ),
        migrations.AlterField(
            model_name='incrementoabastecimiento',
            name='comprador',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='incrementoabastecimiento',
            name='tipo_mercado',
            field=models.IntegerField(choices=[('uno', 'Tradicional'), ('dos', 'Feria'), ('tres', 'Local'), ('cuatro', 'Empresa comercializadora'), ('cinco', 'Empresa procesadora'), ('seis', 'Empresas exportadoras'), ('siete', 'Supermercado'), ('ocho', 'Cadena de restaurantes'), ('nueve', 'Intermediarios')]),
        ),
        migrations.AlterField(
            model_name='mercados',
            name='opciones',
            field=models.IntegerField(choices=[(1, 'Total mercados'), (2, 'Riesgo relacionado con el mercado'), (3, 'Log\xedstica de salida'), (4, 'Estrategias de mercadeo')]),
        ),
        migrations.AlterField(
            model_name='operaciones',
            name='opciones',
            field=models.IntegerField(choices=[(1, 'Total operaciones'), (2, 'Logistica, almacenamiento y tecnolog\xeda'), (3, 'Producci\xf3n'), (4, 'Procesamiento')]),
        ),
        migrations.AlterField(
            model_name='producencomercializan',
            name='cultivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productores.Cultivo'),
        ),
        migrations.AlterField(
            model_name='producencomercializan',
            name='opcion',
            field=models.IntegerField(choices=[(1, 'a) Producen y comercializan de forma colectiva'), (2, 'b) Producen productos sanos'), (3, 'c) Tienen contratos de largo plazo')]),
        ),
        migrations.AlterField(
            model_name='riesgoexternos',
            name='opciones',
            field=models.IntegerField(choices=[(1, 'Total riesgo externo'), (2, 'Conocimiento de riesgos nat. y climat.'), (3, 'Mitigaci\xf3n de riesgos nat. y climat.'), (4, 'Conocimiento de riesgos biol. y amb.'), (5, 'Mitigaci\xf3n de riesgos biol\xf3gicos y amb.')]),
        ),
        migrations.AlterField(
            model_name='sostenibilidad',
            name='opciones',
            field=models.IntegerField(choices=[(1, 'Total sostenibilidad'), (2, 'Aspectos Sociales'), (3, 'Aspectos ambientales')]),
        ),
        migrations.AlterField(
            model_name='suministros',
            name='opciones',
            field=models.IntegerField(choices=[(1, 'Total suministros'), (2, 'Adquisici\xf3n'), (3, 'Log\xedstica de entrada'), (4, 'Contrataci\xf3n de miembros/agr. Ext.'), (5, 'Supervisi\xf3n y cap.de productores'), (6, 'Servicios financieros a miembros')]),
        ),
    ]