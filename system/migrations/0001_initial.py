# Generated by Django 2.1.7 on 2019-12-28 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('sr_no', models.IntegerField()),
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='issued',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateField(auto_now=True)),
                ('return_date', models.DateField()),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Books')),
            ],
        ),
        migrations.CreateModel(
            name='request',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Books')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now=True)),
                ('last_login', models.DateTimeField(null=True)),
                ('password', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='request',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.User'),
        ),
        migrations.AddField(
            model_name='issued',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.User'),
        ),
    ]
