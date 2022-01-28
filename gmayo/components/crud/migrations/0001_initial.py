# Generated by Django 3.2.9 on 2022-01-28 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('parroquia', models.CharField(max_length=200, verbose_name='Parroquia')),
                ('municipio', models.CharField(default='Tucupita', max_length=200, verbose_name='Municipio')),
                ('estado', models.CharField(default='Delta Amacuro', max_length=200, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Responsable',
                'verbose_name_plural': 'Responsables',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('pnf', models.TextField(blank=True, choices=[('Administracion', 'Administracion'), ('Contaduria Publica', 'Contaduria Publica'), ('Turismo', 'Turismo'), ('Agroalimentacion', 'Agroalimentacion'), ('Informatica', 'Informatica'), ('Construccion Civil', 'Construccion Civil'), ('Procesamiento y Distribucion de alimentos', 'Procesamiento y Dist. de alimentos'), ('Terapia Ocupacional', 'Terapia Ocupacional'), ('Fisioterapia', 'Fisioterapia')], default='Aprobado', max_length=41, verbose_name='Carrera')),
                ('estado', models.TextField(blank=True, choices=[('Aprobado', 'Aprobado'), ('En curso', 'En curso'), ('Reprobado', 'Reprobado')], default='Aprobado', max_length=50, verbose_name='Estado')),
                ('year', models.IntegerField(blank=True, choices=[(2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], verbose_name='Año')),
                ('resumen', models.TextField(default='ninguno', max_length=300, verbose_name='Resumen')),
                ('integrantes', models.TextField(default='no disponible', max_length=300, verbose_name='Integrantes')),
                ('upload', models.FileField(max_length=50, upload_to='uploads/%Y/%m/%d/')),
                ('caso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.caso', verbose_name='Caso')),
                ('responsable', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='crud.responsable', verbose_name='Responsable')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
                'ordering': ['id'],
            },
        ),
    ]
