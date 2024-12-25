# Generated by Django 3.2 on 2022-05-21 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product_App', '0002_auto_20220521_0307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('total_seat', models.IntegerField()),
                ('opening', models.CharField(max_length=10)),
                ('closed', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='reservation',
            name='table_types',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Product_App.restaurent'),
        ),
        migrations.DeleteModel(
            name='TableType',
        ),
    ]
