# Generated by Django 4.1.4 on 2023-01-19 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('B_name', models.CharField(max_length=40)),
                ('A_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('S_name', models.CharField(max_length=40)),
                ('S_password', models.CharField(max_length=40)),
                ('S_phone', models.BigIntegerField()),
                ('S_semester', models.IntegerField()),
                ('S_course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.course')),
            ],
        ),
        migrations.CreateModel(
            name='Issue_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('I_date', models.DateField()),
                ('E_date', models.DateField()),
                ('Bk_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.book')),
                ('St_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.student')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='Course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.course'),
        ),
    ]
