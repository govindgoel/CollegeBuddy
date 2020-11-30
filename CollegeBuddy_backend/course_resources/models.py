from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from .validators import validate_file_extension

class Resource_Type(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='Type_Resource', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Resource_Type"
        verbose_name = "Resource_Type"

    def __str__(self):
        return self.name

class Resource_Tag(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='Tag_Resource', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Resource_Tag"
        verbose_name = "Resource_Tag"

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='Branch_Resource', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Branch"
        verbose_name = "Branch"

    def __str__(self):
        return self.name

class Courses(models.Model):
    name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='Course', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Courses"
        verbose_name = "Course"

    def __str__(self):
        return self.name

class Batch(models.Model):
    year = models.CharField(max_length=5)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='Batch', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Batch"
        verbose_name = "Batch"

    def __str__(self):
        return self.year

class Resource(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name='Name of the Resource')
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,related_name='branch')
    date = models.DateField(default=date.today)
    uploader = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Resource', verbose_name='User', null=True, blank=True)
    course = models.ForeignKey(Courses,on_delete=models.CASCADE,related_name='course')
    batch = models.ForeignKey(Batch,on_delete=models.CASCADE,related_name='batch')
    resource_type = models.ForeignKey(Resource_Type,on_delete=models.CASCADE,blank=True,null=True)
    tags = models.ManyToManyField(Resource_Tag, related_name='tags')
    url = models.URLField(max_length=100, default='')
    pdf = models.FileField(upload_to='docs/resources/',blank=True,null=True,validators=[validate_file_extension])
    details = RichTextField(null=True, blank=True, verbose_name='Details')

    class Meta:
        verbose_name_plural = "Resources"
        verbose_name = "Resource"

    def clean(self):
        cleaned_data = super().clean()
        if self.url and self.pdf:
            raise ValidationError('!!__Either provide resource url or the pdf of resource__!!')

    def __str__(self):
        return self.name
