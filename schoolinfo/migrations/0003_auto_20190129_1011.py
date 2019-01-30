# Generated by Django 2.1.5 on 2019-01-29 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schoolinfo', '0002_auto_20190129_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdata',
            name='authorname',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='bookdata',
            name='date_of_publication',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='books',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolinfo.Bookdata'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
