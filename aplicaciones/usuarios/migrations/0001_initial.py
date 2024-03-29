# Generated by Django 4.2.2 on 2023-06-16 15:12

import aplicaciones.usuarios.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200, unique=True, verbose_name='Username')),
                ('nombres', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombres')),
                ('apellidos', models.CharField(blank=True, max_length=200, null=True, verbose_name='Apellidos')),
                ('email', models.EmailField(max_length=150, unique=True, verbose_name='Correo Electronico')),
                ('cedula', models.IntegerField(blank=True, default=0, null=True)),
                ('telefono', models.CharField(blank=True, default='04242020470', max_length=50, null=True, verbose_name='Telefono')),
                ('activo', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('ultimo_ingreso', models.DateTimeField(auto_now=True, verbose_name='actualizado')),
                ('direccion', models.CharField(blank=True, default='Desconocido', max_length=100, null=True, verbose_name='Direccion')),
                ('imagenPerfil', models.ImageField(blank=True, default='media/perfil/default.png', max_length=200, null=True, upload_to=aplicaciones.usuarios.models.foto_perfil_usuarios, verbose_name='Imagen de Perfil')),
                ('rol', models.CharField(blank=True, choices=[('master', 'Master'), ('medico', 'Medico'), ('paciente', 'Paciente')], default='master', max_length=150, null=True, verbose_name='Rol')),
                ('nacionalidad', models.CharField(blank=True, choices=[('venezolano', 'Venezolano'), ('extranjero', 'Extranjero')], default='venezolano', max_length=150, null=True, verbose_name='Nacionalidad')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'usuarios',
                'permissions': [],
            },
        ),
    ]
