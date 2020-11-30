from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField

class Event_Type(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='Type_Author', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Event_Type"
        verbose_name = "Event_Type"

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='Tag_Author', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Tags"
        verbose_name = "Tag"

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name='Title of the event')
    slug = models.CharField(max_length=50, blank=True, verbose_name='Slug')
    content = models.TextField(blank=True, null=True, verbose_name='Content')
    date = models.DateTimeField(verbose_name="Event Date", default=timezone.now)
    creator = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Events', verbose_name='User', null=True, blank=True)
    event_type = models.ForeignKey(Event_Type,on_delete=models.CASCADE,blank=True,null=True)
    tags = models.ManyToManyField(Tag, related_name='tags')
    pinned = models.BooleanField(default=False)
    location = models.CharField(max_length=50, blank=True, verbose_name='Location')
    details = RichTextField(null=True, blank=True, verbose_name='Details')

    class Meta:
        verbose_name_plural = "Events"
        verbose_name = "Event"

    def __str__(self):
        return self.name
