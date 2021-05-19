from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
from taggit.managers import TaggableManager
from embed_video.fields import EmbedVideoField
from core.models import Team
from .modelchoices import features_furnished_choices, feature_choices, state_choices, city_choices,location_choices
from multiselectfield import MultiSelectField


class Item(models.Model):
    
    video = EmbedVideoField()  # same like models.URLField()
    item_snippet = models.CharField(max_length=250, default="click to read the blog post ")
    
class Category(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    is_active = models.BooleanField(default=True)
    is_selected = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        """ Meta for the naming in the django admin that
            describes a model if the object is singular or
            plural
        """
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    def get_absolute_url(self):
        return reverse("categories", args=[ self.slug ])


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')
    
class Post(models.Model):
    STATUS_CHOICES= ( ('draft','Draft'),('published','Published'),
                      )
    TYPE_CHOICES= ( ('rent','Rent'),('lease','Lease'),
                      )
    
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(Team,on_delete=models.CASCADE)
    estate_type = models.CharField(max_length=10,choices=TYPE_CHOICES,default='rent')
    address = models.CharField(max_length=100)
    location = models.CharField(max_length=100, choices=location_choices)
    city = models.CharField(max_length=70, choices=city_choices)
    feature_type = MultiSelectField(choices=features_furnished_choices)
    #category = models.CharField(max_length=250, default="Others")
    snippet = models.CharField(max_length=250, default="click to read the blog post ")
    price = models.IntegerField(blank=True , null=True)
    bedrooms = models.IntegerField(blank=True , null=True)
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1,blank=True , null=True)
    garage = models.IntegerField(default=0)
    sqmt = models.IntegerField(blank=True , null=True)
    lot_size = models.DecimalField(max_digits=5, decimal_places=1, blank=True , null=True)
    post_photo = models.ImageField(upload_to='photos/listings/', blank=True , null=True)
    post_photo_1 = models.ImageField(upload_to='photos/listings/', blank=True , null=True)
    post_photo_2 = models.ImageField(upload_to='photos/listings/', blank=True , null=True)
    post_photo_3 = models.ImageField(upload_to='photos/listings/', blank=True , null=True)
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)
    video = EmbedVideoField(blank=True, null=True)  # same like models.URLField()
    youtube_link = models.URLField(max_length=130, blank=True, null=True)
    longtitude = models.DecimalField(decimal_places=3, max_digits=10, null=True, blank=True)
    latitude = models.DecimalField(decimal_places=3, max_digits=10, null=True, blank=True)
    url_link = models.URLField(max_length=280, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse('listing',
                    args=[self.pk])
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title