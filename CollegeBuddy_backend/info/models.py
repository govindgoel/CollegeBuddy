from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from course_resources.validators import validate_file_extension


class Notice(models.Model):
    title = models.CharField(max_length=50)
    pinned = models.BooleanField()
    date = models.DateField(default=date.today)
    url = models.URLField(max_length=100, default='')
    pdf = models.FileField(upload_to='docs/info/',blank=True,null=True,validators=[validate_file_extension])
    details = RichTextField(null=True, blank=True, verbose_name='Details')

    class Meta:
        verbose_name_plural = "Notice"
        verbose_name = "Notice"

    def clean(self):
        cleaned_data = super().clean()
        if self.url and self.pdf:
            raise ValidationError('!!__Either provide resource url or the pdf of resource__!!')

    def __str__(self):
        return self.title
