from django.db import models
from django.utils.html import format_html
from produtos.models import Course, Group
from cpf_field.models import CPFField


class Student(models.Model):
    photo = models.ImageField(upload_to='photos/students/', verbose_name='foto')
    """
    :rtype photo: str
    """
    name = models.CharField(max_length=90, verbose_name='nome')
    """
    :rtype name: str
    """
    cpf = CPFField('cpf')
    """
    :rtype cpf: str
    """
    email = models.EmailField(verbose_name='e-mail')
    """
    :rtype email: str
    """
    course = models.ForeignKey(Course, on_delete=models.PROTECT, verbose_name='curso')
    """
    :rtype course: str
    """
    group = models.ForeignKey(Group, on_delete=models.PROTECT, verbose_name='turma')
    """
    :rtype group: str
    """

    def photo_preview(self):
        """
        Returns an HTML <img> tag with 'self.photo.url' and '100px' as src and width attributes, respectively.

        :return: An HTML <img> tag.
        :rtype: str
        """
        return format_html(f'<img src="{self.photo.url}" width="100px" />')

    photo_preview.short_description = 'foto'
    photo_preview.allow_tags = True

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'estudante'


class Teacher(models.Model):
    photo = models.ImageField(upload_to='photos/teachers/', verbose_name='foto')
    """
    :rtype photo: str
    """
    cpf = CPFField('cpf')
    """
    :rtype cpf: str
    """
    name = models.CharField(max_length=90, verbose_name='nome')
    """
    :rtype name: str
    """
    email = models.EmailField(verbose_name='e-mail')
    """
    :rtype email: str
    """
    groups = models.ManyToManyField('produtos.Group', related_name='classes_on_teachers', verbose_name='turmas')
    """
    :rtype groups: str
    """

    def photo_preview(self):
        """
        Returns an HTML <img> tag with 'self.photo.url' and '100px' as src and width attributes, respectively.

        :return: An HTML <img> tag.
        :rtype: str
        """
        return format_html(f'<img src="{self.photo.url}" width="100px" />')

    photo_preview.short_description = 'foto'
    photo_preview.allow_tags = True

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'professore'
