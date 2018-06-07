# Create your models here.
#from django.contrib.auth.decorators import LoginRequired
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator,MaxLengthValidator
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.http import request

class User(AbstractUser):
    username=models.CharField(max_length=20,default="")
    email = models.EmailField(_('email address'), unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                     message="Phone number must be entered in the format: '+999999999'.Min 9 to Max 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17)  # validators should be a list

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __unicode__(self):
        return self.email

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

    def __str__(self):
        return self.email



class Setupuser(models.Model):
    your_nickname=models.CharField(max_length=30,blank=False,null=True)
    your_organization=models.CharField(max_length=200,blank=False,null=True)
    your_phone_no=models.CharField(max_length=20,blank=False,null=True)
    email_id=models.CharField(max_length=200,blank=False,unique=True)
    CEO = 'CEO'
    GENERAL_MANAGER = 'GM'
    ASST_MANAGER = 'AM'
    PROJECT_MANAGER = 'PM'
    TEAM_LEAD = "TL"
    FRESHER="FR"
    JCHOICES = (
        (CEO, 'CEO'),
        (GENERAL_MANAGER, 'General Manager'),
        (ASST_MANAGER, 'Assistant Manager'),
        (PROJECT_MANAGER, 'Project Manager'),
        (TEAM_LEAD, 'Team Leader'))
    your_designation = models.CharField(choices=JCHOICES,max_length=20)

    LEVEL1 = "L1"
    LEVEL2 = "L2"
    LEVEL3 = "L3"
    LEVEL4 = "L4"
    NJ = "Newly Joined"
    LCHOICES = (
        (LEVEL1,"Level 1"),
        (LEVEL2,"Level 2"),
        (LEVEL3,"Level 3"),
        (LEVEL4,"Level 4"),
        (NJ,"Newly joined"),
              )
    your_job_level=models.CharField(max_length=13,choices=LCHOICES)
    share_KB_with = models.ManyToManyField(User)



class Buildkb(models.Model):
    email=models.CharField(max_length=200,blank=False)
    knowledge_category=models.CharField(max_length=50,blank=True)
    title=models.CharField(max_length=500,blank=True)
    knowledge=models.TextField(blank=False)
    keywords=models.TextField(blank=True,null=True)
    share_with=models.ManyToManyField(User)

    def __str__(self):
        return self.knowledge



