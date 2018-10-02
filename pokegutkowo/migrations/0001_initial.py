# Generated by Django 2.1.2 on 2018-10-02 18:40

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import pokegutkowo.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=255, verbose_name='Nick')),
                ('level', models.IntegerField(verbose_name='Poziom')),
                ('team', models.CharField(choices=[('instinct', 'Instinct'), ('mystic', 'Mystic'), ('valor', 'Valor')], max_length=255, verbose_name='Zespół')),
                ('trainer_code', models.CharField(blank=True, max_length=12, null=True, verbose_name='Kod trenera')),
            ],
            options={
                'verbose_name': 'Gracz',
                'verbose_name_plural': 'Gracze',
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Nazwa strony')),
                ('owner_about', ckeditor.fields.RichTextField(verbose_name='O właścicielu')),
                ('owner_screenshot', models.ImageField(upload_to='', verbose_name='Screenshot właściciela')),
                ('discord', models.URLField(max_length=255, verbose_name='Link do discorda')),
                ('owner_acc', models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.CASCADE, to='pokegutkowo.Players')),
            ],
            options={
                'verbose_name': 'Ustawienia',
                'verbose_name_plural': 'Ustawienia',
            },
            bases=(pokegutkowo.models.SingleInstanceMixin, models.Model),
        ),
    ]
