# Generated by Django 2.2.2 on 2019-09-04 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_record_rna_seq'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='RNA_seq',
            new_name='RNA_Seq',
        ),
    ]
