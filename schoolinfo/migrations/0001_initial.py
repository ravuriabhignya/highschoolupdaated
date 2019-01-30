# Generated by Django 2.1.5 on 2019-01-29 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookdata',
            fields=[
                ('title', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('authorname', models.CharField(max_length=30)),
                ('date_of_publication', models.DateField()),
                ('number_of_pages', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Schooldata',
            fields=[
                ('region', models.IntegerField(default=100)),
                ('school_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=70, unique=True)),
                ('principal_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=8)),
                ('address', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Studentdata',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=70, unique=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolinfo.Bookdata')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolinfo.Schooldata')),
            ],
        ),
    ]
