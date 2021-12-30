# Generated by Django 3.2.9 on 2021-11-29 22:48

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
            options={
                'verbose_name': 'Ubicacion',
                'verbose_name_plural': 'Ubicaciones',
                'ordering': ['id'],
            },
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
                ('pnf', models.CharField(max_length=200, verbose_name='Carrera')),
                ('estado', models.CharField(choices=[('Aprobado', 'Aprobado'), ('En curso', 'En curso'), ('Reprobado', 'Reprobado')], default='Aprobado', max_length=10)),
                ('year', models.IntegerField(blank=True, choices=[(1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020)])),
                ('resumen', models.CharField(default='ninguno', max_length=300, verbose_name='Resumen')),
                ('integrantes', models.CharField(default='no disponible', max_length=300, verbose_name='Integrantes')),
                ('upload', models.FileField(blank=True, upload_to='uploads/%Y/%m/%d/')),
                ('user', models.CharField(max_length=300)),
                ('caso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.caso', verbose_name='Caso')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.responsable', verbose_name='Responsable')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
                'ordering': ['id'],
            },
        ),
    ]
