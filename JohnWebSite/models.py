from django.db import models


class ExtUser(models.Model):
    objects = None

    class Meta:
        verbose_name = 'Юзер'
        verbose_name_plural = 'Юзер'

    helloExtUser = models.CharField(verbose_name='Приветствие на первом экране', max_length=255)
    descriptionExtUser = models.TextField(verbose_name='Описание на первом экране', max_length=1000)
    pictureExtUser = models.FileField(verbose_name='Картинка на первом экране', upload_to='JohnWebSite/img/user',
                                      null=True, blank=True)
    resumeExtUser = models.FileField(verbose_name='Файл резюме', upload_to='JohnWebSite/resume', null=True, blank=True)

    def __str__(self):
        return self.helloExtUser


class Social(models.Model):
    objects = None

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'

    titleSocial = models.CharField(verbose_name='Название социальной сети', max_length=100)
    pictureSocial = models.FileField(verbose_name='Картинка социальной сети', upload_to='JohnWebSite/img/social')
    linkSocial = models.URLField(verbose_name='Ссылка на социальную сеть', max_length=255, unique=True)

    def __str__(self):
        return self.titleSocial


class Blog(models.Model):
    objects = None

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['-createdBlog']

    titleBlog = models.CharField(verbose_name='Название блога', max_length=100)
    subtitleBlog = models.CharField(verbose_name='Категория? блога', max_length=100)
    descriptionBlog = models.TextField(verbose_name='Описание блога')
    createdBlog = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    changedBlog = models.DateField(verbose_name='Дата последнего измения', auto_now=True)
    activeBlog = models.BooleanField(verbose_name='Публикуем?', default=True)
    pictureBlog = models.FileField(verbose_name='Картинка блога', upload_to='JohnWebSite/img/blog', blank=True)
    linkBlog = models.URLField(verbose_name='Адрес блога в интернете', max_length=255, blank=True)

    def __str__(self):
        return f'{self.titleBlog} {self.activeBlog}'


class Project(models.Model):
    objects = None

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['-createdProject']

    titleProject = models.CharField(verbose_name='Название проекта', max_length=100)
    subtitleProject = models.CharField(verbose_name='Категория? проекта', max_length=100)
    descriptionProject = models.TextField(verbose_name='Описание проекта')
    createdProject = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    activeProject = models.BooleanField(verbose_name='Публикуем?', default=True)
    pictureProject = models.FileField(verbose_name='Картинка проекта', upload_to='JohnWebSite/img/project', blank=True)
    linkProject = models.URLField(verbose_name='Адрес проекта в интернете', max_length=255, unique=True)

    def __str__(self):
        return f'{self.titleProject} {self.linkProject}'
