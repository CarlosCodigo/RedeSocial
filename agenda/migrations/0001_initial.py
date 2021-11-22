# Generated by Django 3.2.8 on 2021-11-21 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgendamentoInicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Disciplinas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dF', models.CharField(choices=[('Selecione', 'Selecione'), ('Artes', 'Artes'), ('Ciências', 'Ciências'), ('Ed.Fisica', 'Ed.Fisica'), ('Geografia', 'Geografia'), ('História', 'História'), ('Inglês', 'Inglês'), ('Matemática', 'Matemática'), ('Português', 'Português')], max_length=20, verbose_name='Disciplinas do Fundamental')),
                ('dM', models.CharField(choices=[('Selecione', 'Selecione'), ('Artes', 'Artes'), ('Biologia', 'Biologia'), ('Ed.Fisica', 'Ed.Fisica'), ('Espanhol', 'Espanhol'), ('Filosofia', 'Filosofia'), ('Geografia', 'Geografia'), ('História', 'História'), ('Inglês', 'Inglês'), ('Matemática', 'Matemática'), ('Português', 'Português'), ('Quimica', 'Quimica'), ('Sociologia', 'Sociologia')], max_length=20, verbose_name='Disciplinas do Médio')),
            ],
            options={
                'verbose_name': 'Disciplinas',
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profF', models.CharField(choices=[], max_length=20, verbose_name='professores Fundamental(as)')),
                ('profM', models.CharField(choices=[], max_length=20, verbose_name='professores Médio(as)')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agenda.disciplinas', verbose_name='disciplinas')),
            ],
            options={
                'verbose_name': 'Professor',
            },
        ),
    ]
