from django.db import models
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, name,sex,email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
        	name = name,
            sex = sex,
            email=self.normalize_email(email),            
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,name,sex,email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(name,
        	sex,  
        	email,     	
        	password=password,
            date_of_birth=date_of_birth
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    Face = models.ImageField(upload_to='profileImg',blank=True)
    SEX = (('男','Male'),('女','Female'))
    sex = models.CharField(max_length=1, choices=SEX)
    school = models.CharField(max_length=10)
    major = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    name = models.CharField(max_length=10)
    objects = MyUserManager()
    talent= models.CharField(max_length=90,blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','sex','date_of_birth']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.name

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    def image_tag(self):
        return u'<img src="%s" width="60px" />' % self.img_file.url  
    # 欄位名稱

    image_tag.short_description = _('image')
    # 允許執行 image_tag 中回傳的 html 語法，若為 False(預設)則會被視為純文字

    image_tag.allow_tags = True