# Generated by Django 2.1.2 on 2018-10-25 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_num', models.DecimalField(decimal_places=2, max_digits=20)),
                ('price_unit', models.CharField(max_length=200)),
                ('ingredient', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='recipe.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=200)),
                ('location', models.CharField(default='Safeway', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='history',
            name='store',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='grocery.Store'),
        ),
    ]