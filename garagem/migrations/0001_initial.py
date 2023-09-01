# Generated by Django 4.2.4 on 2023-09-01 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acessorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Acessório',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Cores',
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='modelos', to='garagem.categoria')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='modelos', to='garagem.marca')),
            ],
            options={
                'verbose_name_plural': 'Modelos',
            },
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(default='', max_length=100)),
                ('preco', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('ano', models.IntegerField(blank=True, null=True)),
                ('acessorios', models.ManyToManyField(related_name='veiculos', to='garagem.acessorio')),
                ('cor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='veiculos', to='garagem.cor')),
                ('imagem', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='uploader.image')),
                ('modelo', models.ForeignKey(blank=True, default=2, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='veiculos', to='garagem.modelo')),
            ],
            options={
                'verbose_name': 'Veículo',
            },
        ),
    ]
