import django.db.models.deletion
from django.db import migrations, models


def migrar_professores(apps, schema_editor):
    Material = apps.get_model('uninotesapp', 'Material')
    Professor = apps.get_model('uninotesapp', 'Professor')

    db = schema_editor.connection.alias

    for material in Material.objects.using(db).all():
        nome = (material.professor_nome or '').strip()

        if nome:
            professor, criado = Professor.objects.using(db).get_or_create(
                name=nome
            )

            Material.objects.using(db).filter(
                pk=material.pk
            ).update(professor_id=professor.pk)


class Migration(migrations.Migration):

    dependencies = [
        ('uninotesapp', '0010_aluno_professor'),
    ]

    operations = [

        migrations.RemoveField(
            model_name='material',
            name='avaliacao',
        ),

        # Preserva os nomes antigos
        migrations.RenameField(
            model_name='material',
            old_name='professor',
            new_name='professor_nome',
        ),

        # Cria o novo relacionamento
        migrations.AddField(
            model_name='material',
            name='professor',
            field=models.ForeignKey(
                to='uninotesapp.professor',
                on_delete=django.db.models.deletion.PROTECT,
                null=True,
                blank=True,
            ),
        ),

        # Associa os materiais aos professores
        migrations.RunPython(
            migrar_professores,
            migrations.RunPython.noop,
        ),

        # Remove o campo antigo
        migrations.RemoveField(
            model_name='material',
            name='professor_nome',
        ),

        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('avaliacao', models.IntegerField(
                    choices=[
                        (0, 'Sem avaliação'),
                        (1, '⭐'),
                        (2, '⭐⭐'),
                        (3, '⭐⭐⭐'),
                        (4, '⭐⭐⭐⭐'),
                        (5, '⭐⭐⭐⭐⭐')
                    ],
                    default=0
                )),
                ('material', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='avaliacoes',
                    to='uninotesapp.material'
                )),
            ],
        ),

        migrations.CreateModel(
            name='Materiais_salvos',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('visualizacoes', models.PositiveIntegerField(default=0)),
                ('downloads', models.PositiveIntegerField(default=0)),
                ('aluno', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='Meus_materiais',
                    to='uninotesapp.aluno'
                )),
                ('material', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='publicacoes',
                    to='uninotesapp.material'
                )),
            ],
        ),
    ]