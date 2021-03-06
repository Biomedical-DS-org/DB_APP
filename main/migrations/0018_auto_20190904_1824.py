# Generated by Django 2.2.2 on 2019-09-04 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20190804_1210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='Location_1',
            new_name='Macular_Biopsy',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='Location_2',
            new_name='Macular_Biopsy_Location',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='Location_3',
            new_name='Macular_Slides',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='Location_4',
            new_name='Macular_Slides_Location',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='Tissue_1',
            new_name='Retinal_Biopsy',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='Tissue_2',
            new_name='Retinal_Biopsy_Location',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='Tissue_3',
            new_name='Retinal_Slides',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='Tissue_4',
            new_name='Retinal_Slides_Location',
        ),
    ]
