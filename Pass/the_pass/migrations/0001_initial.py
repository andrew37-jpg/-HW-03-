# Generated by Django 5.0.6 on 2024-05-30 19:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=10, verbose_name='Широта')),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=10, verbose_name='Долгота')),
                ('height', models.IntegerField(verbose_name='Высота')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.CharField(choices=[('2Б', '2Б'), ('2А', '2А'), ('3А', '3А'), ('1А', '1А'), ('1Б', '1Б'), ('3Б', '3Б')], default='1А', max_length=2, verbose_name='Зима')),
                ('summer', models.CharField(choices=[('2Б', '2Б'), ('2А', '2А'), ('3А', '3А'), ('1А', '1А'), ('1Б', '1Б'), ('3Б', '3Б')], default='1А', max_length=2, verbose_name='Лето')),
                ('autumn', models.CharField(choices=[('2Б', '2Б'), ('2А', '2А'), ('3А', '3А'), ('1А', '1А'), ('1Б', '1Б'), ('3Б', '3Б')], default='1А', max_length=2, verbose_name='Осень')),
                ('spring', models.CharField(choices=[('2Б', '2Б'), ('2А', '2А'), ('3А', '3А'), ('1А', '1А'), ('1Б', '1Б'), ('3Б', '3Б')], default='1А', max_length=2, verbose_name='Весна')),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('fam', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('otc', models.CharField(max_length=50, verbose_name='Отчество')),
                ('phone', models.CharField(max_length=15, verbose_name='Телефон')),
            ],
        ),
        migrations.CreateModel(
            name='Pereval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('NW', 'новый'), ('RJ', 'отклонён'), ('PN', 'в работе'), ('AC', 'принят')], default='NW', max_length=2)),
                ('beauty_name', models.CharField(default='пер.', max_length=255)),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('other_titles', models.CharField(max_length=255, verbose_name='Альтернативное название')),
                ('connect', models.CharField(max_length=500, verbose_name='Что соединяет')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('coords', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='the_pass.coords', verbose_name='Координаты')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='the_pass.level', verbose_name='Уровень сложности')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='the_pass.myuser', verbose_name='Автор')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=2000, verbose_name='ссылка на изображение')),
                ('title', models.TextField(verbose_name='Описание изображения')),
                ('pereval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='the_pass.pereval', verbose_name='Изображения')),
            ],
        ),
    ]
