# Generated by Django 2.1.2 on 2018-10-27 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ingredient', '0001_initial'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_num', models.DecimalField(decimal_places=2, max_digits=20)),
                ('price_unit', models.CharField(max_length=200)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredient.Ingredient')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Store')),
            ],
        ),
    ]