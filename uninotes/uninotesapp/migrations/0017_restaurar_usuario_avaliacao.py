import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('uninotesapp', '0016_visualizacao_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacao',
            name='usuario',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddConstraint(
            model_name='avaliacao',
            constraint=models.UniqueConstraint(
                fields=('material', 'usuario'),
                name='uma_avaliacao_por_usuario_e_material',
            ),
        ),
    ]