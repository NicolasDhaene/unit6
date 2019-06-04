# Generated by Django 2.2.1 on 2019-05-31 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minerals', '0002_auto_20190530_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mineral',
            name='img_caption',
        ),
        migrations.RemoveField(
            model_name='mineral',
            name='img_filename',
        ),
        migrations.RemoveField(
            model_name='mineral',
            name='mohs_hardness',
        ),
        migrations.AddField(
            model_name='mineral',
            name='image_caption',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='mineral',
            name='image_filename',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='mineral',
            name='mohs_scale_hardness',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='category',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='cleavage',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='color',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='crystal_habit',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='crystal_symmetry',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='crystal_system',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='diaphaneity',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='formula',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='luster',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='optical_properties',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='refractive_index',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='specific_gravity',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='streak',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='strunz_classification',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='unit_cell',
            field=models.CharField(max_length=255, null=True),
        ),
    ]