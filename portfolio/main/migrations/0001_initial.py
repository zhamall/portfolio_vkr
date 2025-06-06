# Generated by Django 5.2 on 2025-04-29 08:22

import django.db.models.deletion
import main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('about', models.TextField()),
                ('links', models.URLField(blank=True)),
            ],
            options={
                'verbose_name': 'Resume',
                'verbose_name_plural': 'Resume',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project_images/')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.project')),
            ],
        ),
        migrations.CreateModel(
            name='ResumeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='resume_images/')),
                ('resume', models.ForeignKey(default=main.models.Resume.get_solo, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.resume')),
            ],
        ),
        migrations.CreateModel(
            name='ResumeLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название ссылки')),
                ('url', models.URLField(verbose_name='URL ссылки')),
                ('resume', models.ForeignKey(default=main.models.Resume.get_solo, on_delete=django.db.models.deletion.CASCADE, related_name='resume_links', to='main.resume')),
            ],
        ),
        migrations.AddField(
            model_name='resume',
            name='skills',
            field=models.ManyToManyField(related_name='skill', to='main.tag'),
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(related_name='projects', to='main.tag'),
        ),
    ]
