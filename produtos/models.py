from datetime import datetime

from django.db import models


class Theme(models.Model):
    name = models.CharField(max_length=50, verbose_name='nome')
    """
    :rtype name: str
    """
    description = models.TextField(blank=True, null=True, verbose_name='descrição')
    """
    :rtype description: str
    """

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'disciplina'


class Course(models.Model):
    name = models.CharField(max_length=90, verbose_name='nome')
    """
    :rtype name: str
    """
    description = models.TextField(blank=True, null=True, verbose_name='descrição')
    """
    :rtype description: str
    """
    themes = models.ManyToManyField('produtos.Theme', related_name='themes_on_courses', verbose_name='disciplinas')
    """
    :rtype themes: str
    """

    def get_themes(self):
        """
        Retorna uma lista de disciplinas (themes) como strings.

        :return: A lista de disciplinas (themes).
        :rtype: list[str]
        """
        return ", ".join([theme.name for theme in self.themes.all()])

    get_themes.short_description = 'disciplinas'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'curso'


class Group(models.Model):
    name = models.CharField(max_length=10, verbose_name='nome')
    """
    :rtype name: str
    """
    data_of_register = models.DateField(default=datetime.now(), verbose_name='data de Início')
    """
    :rtype data_of_register: str
    """

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'turma'
