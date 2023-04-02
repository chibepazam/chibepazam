# Generated by Django 4.1.7 on 2023-04-02 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the food.', max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The ingredient name.', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FoodIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.food')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.ingredient')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='ingredients',
            field=models.ManyToManyField(through='foods.FoodIngredient', to='foods.ingredient'),
        ),
    ]