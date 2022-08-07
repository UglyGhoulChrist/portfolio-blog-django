from django.db import models


# User имеет поля приветствие, описание, фотографию, файл резюме
class ExtUser(models.Model):
    objects = None

    class Meta:
        verbose_name = 'Юзер'
        verbose_name_plural = 'Юзеры'

    helloExtUser = models.CharField(verbose_name='Приветствие на первом экране', max_length=255)
    descriptionExtUser = models.CharField(verbose_name='Описание на первом экране', max_length=255)
    pictureExtUser = models.FileField(verbose_name='Картинка на первом экране', upload_to='JohnWebSite/img', null=True,
                                      blank=True)
    resumeExtUser = models.FileField(verbose_name='Файл резюме', upload_to='JohnWebSite/resume', null=True, blank=True)

    def __str__(self):
        return self.helloExtUser


# Ссылки на социальные сети будет иметь поля название, картинка, ссылка на адрес в интернете
class Social(models.Model):
    objects = None

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'

    titleSocial = models.CharField(verbose_name='Название социальной сети', max_length=255)
    pictureSocial = models.FileField(verbose_name='Картинка социальной сети', upload_to='JohnWebSite/img', null=True,
                                     blank=True)
    linkSocial = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.titleSocial


# Блог имеет поля Название, Краткое описание(категория?), Подробное описание, создан, изменён, актуальность(опубликован или нет)
class Blog(models.Model):
    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['-createdBlog']

    titleBlog = models.CharField(verbose_name='Название блога', max_length=100)
    subtitleBlog = models.CharField(verbose_name='Краткое описание (категория?)', max_length=100)
    descriptionBlog = models.TextField(verbose_name='Описание блога')
    createdBlog = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    changedBlog = models.DateTimeField(verbose_name='Изменён', auto_now=True)
    activeBlog = models.BooleanField(verbose_name='Опубликован', default=True, null=True)

    def __str__(self):
        return f'{self.titleBlog} {self.activeBlog}'


# Проект имеет поля Название, Краткое описание(категория?), Подробное описание, создан, Картинка проекта, Адрес проекта в интернете
class Project(models.Model):
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    titleProject = models.CharField(verbose_name='Название проекта', max_length=100)
    subtitleProject = models.CharField(verbose_name='Краткое описание(категория?)', max_length=100)
    descriptionProject = models.TextField(verbose_name='Описание проекта')
    createdProject = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    pictureProject = models.FileField(verbose_name='Картинка проекта', upload_to='JohnWebSite/img', null=True,
                                      blank=True)
    linkProject = models.SlugField(max_length=255, unique=True, verbose_name='Адрес проекта в интернете')

    def __str__(self):
        return f'{self.titleProject} {self.linkProject}'
