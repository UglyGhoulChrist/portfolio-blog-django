# Generated by Django 4.1 on 2022-08-06 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleBlog', models.CharField(max_length=100, verbose_name='Название блога')),
                ('subtitleBlog', models.CharField(max_length=100, verbose_name='Краткое описание (категория?)')),
                ('descriptionBlog', models.TextField(verbose_name='Описание блога')),
                ('createdBlog', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('changedBlog', models.DateTimeField(auto_now=True, verbose_name='Изменён')),
                ('activeBlog', models.BooleanField(default=True, null=True, verbose_name='Опубликован')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
            },
        ),
        migrations.CreateModel(
            name='ExtUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('helloExtUser', models.CharField(max_length=255, verbose_name='Приветствие на первом экране')),
                ('descriptionExtUser', models.CharField(max_length=255, verbose_name='Описание на первом экране')),
                ('pictureExtUser', models.FileField(blank=True, null=True, upload_to='JohnWebSite/img', verbose_name='Картинка на первом экране')),
                ('resumeExtUser', models.FileField(blank=True, null=True, upload_to='JohnWebSite/resume', verbose_name='Файл резюме')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleProject', models.CharField(max_length=100, verbose_name='Название проекта')),
                ('subtitleProject', models.CharField(max_length=100, verbose_name='Краткое описание(категория?)')),
                ('descriptionProject', models.TextField(verbose_name='Описание проекта')),
                ('createdProject', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('pictureProject', models.FileField(blank=True, null=True, upload_to='JohnWebSite/img', verbose_name='Картинка проекта')),
                ('linkProject', models.SlugField(max_length=255, unique=True, verbose_name='Адрес проекта в интернете')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleSocial', models.CharField(max_length=255, verbose_name='Название социальной сети')),
                ('pictureSocial', models.FileField(blank=True, null=True, upload_to='JohnWebSite/img', verbose_name='Картинка социальной сети')),
                ('linkSocial', models.SlugField(max_length=255, unique=True)),
            ],
        ),
    ]