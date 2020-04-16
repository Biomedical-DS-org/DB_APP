# Generated by Django 2.2.2 on 2019-07-23 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20190719_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='AMD',
            field=models.CharField(choices=[('No', 'No'), ('Early', 'Early'), ('Borderline', 'Borderline'), ('Late', 'Late'), ('Wet', 'Wet'), ('Unknown', 'Unknown'), ('Not Clincial', 'Not Clincial'), ('Non Control', 'Non Control')], max_length=9),
        ),
        migrations.AlterField(
            model_name='record',
            name='COD',
            field=models.CharField(choices=[('Known', 'Known'), ('Unknown', 'Unknown')], max_length=9),
        ),
        migrations.AlterField(
            model_name='record',
            name='date_processed',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='haplotype_1',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='record',
            name='haplotype_2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='record',
            name='probability',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
