# Generated by Django 4.2.4 on 2023-08-20 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_organization', models.CharField(max_length=120, verbose_name='Name of organization')),
                ('major', models.CharField(max_length=120, verbose_name='A major in this organization')),
                ('description', models.TextField(verbose_name='Description of the major')),
                ('start_at', models.DateTimeField(verbose_name='Date of start your education')),
                ('end_at', models.DateTimeField(blank=True, verbose_name="Date of end your education (If not the end that don't write a date)")),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_organization', models.CharField(max_length=120, verbose_name='Name of organization')),
                ('position', models.CharField(max_length=120, verbose_name='A position in this organization')),
                ('description', models.TextField(verbose_name='Description of the job')),
                ('start_at', models.DateTimeField(verbose_name='Date of start your experience')),
                ('end_at', models.DateTimeField(blank=True, verbose_name="Date of end your experience (If not the end that don't write a date)")),
            ],
        ),
        migrations.AlterField(
            model_name='Experience',
            name='end_at',
            field=models.DateTimeField(null=True, blank=True)
        ),
        migrations.AlterField(
            model_name='Education',
            name='end_at',
            field=models.DateTimeField(null=True, blank=True)
        )
    ]
