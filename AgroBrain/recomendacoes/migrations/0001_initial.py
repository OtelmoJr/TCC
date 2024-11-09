# Generated by Django 5.1.3 on 2024-11-09 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoSolo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ph_min', models.DecimalField(decimal_places=1, max_digits=3)),
                ('ph_max', models.DecimalField(decimal_places=1, max_digits=3)),
                ('mo_min', models.DecimalField(decimal_places=1, max_digits=3)),
                ('mo_max', models.DecimalField(decimal_places=1, max_digits=3)),
                ('fosforo_min', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fosforo_max', models.DecimalField(decimal_places=2, max_digits=5)),
                ('potassio_min', models.DecimalField(decimal_places=2, max_digits=5)),
                ('potassio_max', models.DecimalField(decimal_places=2, max_digits=5)),
                ('calcio_min', models.DecimalField(decimal_places=2, max_digits=5)),
                ('calcio_max', models.DecimalField(decimal_places=2, max_digits=5)),
                ('magnesio_min', models.DecimalField(decimal_places=2, max_digits=5)),
                ('magnesio_max', models.DecimalField(decimal_places=2, max_digits=5)),
                ('saturacao_bases', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
