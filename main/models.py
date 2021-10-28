from _typeshed import OpenBinaryModeReading
from os import name
from django.db import models
from django.contrib.auth.models import User #bringing in a built in user model w/signals
from django.template.defaultfilters import slugify, title #need for blog and portfolio
from ckeditor.fields import RichTextField #richtext field for blog and porfolio

# Create your models here.
# database tables
class Skill(models.Model):
    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'

    #name of the skill
    name = models.CharField(max_length=20, blank=True, null=True)

    #quanative represation of the skill
    score = models.IntegerField(default=80, blank=True, null=True)

    #svg images for key skills
    image = models.FileField(blank=True, null=True, upload_to="skills")

    #if true object will represent a key skill; false represent a coding skill
    is_key_still = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'

    #extends the bulit_in user model with only one user profile(us)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #profile avatar creating a dir to same avatar images
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")

    # title of bio
    title = models.CharField(max_length=200, blank=True, null=True)

    # text written to bio
    bio = models.TextField(blank=True, null=True)

    # many skills
    skills = models.ManyToManyField(Skill, blank=True)

    # file field uploaded to the new cv directory
    cv  = models.FileField(blank=True, null=True, upload_to="cv")

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'
    
class ContactProfile(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ["timestamp"]

    #
    timestamp = models.DateTimeField(auto_now_add=True)

    #
    name = models.CharField(verbose_name="Name", max_length=75)
    
    #
    email = models.EmailField(verbose_name="Email")

    #
    message = models.TextField(verbose_name="Message")
    
    def __str__(self) -> str:
        return f'{self.name}'

class Testimonials(models.Model):#coverletter
    class Meta:
        verbose_name_plurals = 'Testimonials'
        verbose_name = 'Testimonial'
        ordering = ["name"]
    thumbnail = models.ImageField(blank=True, null=True, upload_to = 'Testimonial')
    name = models.CharField(max_length=200, blank=True, null = True)
    role = models.CharField(max_length=200, blank=True, null = True)
    quote = models.CharField(max_length=600, blank=True, null = True)

    #controls the web_site view
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.name}'

class Media(models.Model):

    class Meta:
        verbose_name_plural = 'Media Files'
        verbose_name = 'Media'
        ordering = ["name"]

    image = models.ImageField(blank = True, null=True, upload_to = "media")
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length= 200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self,*args, **kwargs):
        if self.url:
            self.is_image =False
        super(Media, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

class Portfolio(models.Model):
    class Meta:
        verbose_name_plural = 'Portfolios'
        verbose_name = 'Portfolio'
        ordering  = ["name"]

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(max_length=600, blank=True, null=True)

    #richtexteditor the will be updating in admin page rendered to Html
    body = RichTextField(max_length=600, blank=True, null=True)

    image = models.ImageField(blank=True, null=True, upload_to= "portfolio")

    #will populate when saved
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self,*args, **kwargs):
        if not self.id:
           self.slug = slugify(self.name)#refactor all to lowercase and spaces to underscore
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return f'/portfolio/{self.slug}'
    
class Blog(models.Model):
    
    class Meta(models.Model):
        verbose_name_plural = 'Blogs'
        verbose_name = 'Blog'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200,blank=True,null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(max_length=600, blank=True, null=True)
    body = RichTextField(max_length=600, blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to= "blog")
    is_active = models.BooleanField(default=True)

    def save(self,*args, **kwargs):
        if not self.id:
           self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f'/blog/{self.slug}'

class Certificate(models.Model):

    class Meta:
        verbose_name_plural = 'Certificates'
        verbose_name = 'Certificate'

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=100,blank=True,null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=600, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'


    
