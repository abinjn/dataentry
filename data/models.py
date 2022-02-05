
KIT = (
    ('GH', 'Ghubra Centre'),
    ('WA', 'Wadikabir Centre'),
    ('NI', 'Nizwa Centre'),
)
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import ModelState
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.core.validators import RegexValidator



class Profile(models.Model):
    #phone_regex = RegexValidator(regex=r'^\d{8,8}$', message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.")
    
    name = models.CharField(max_length=50, verbose_name='Name', default="")
    grade = models.CharField(max_length=5, verbose_name='Grade', default='')
    school = models.CharField(max_length=20, verbose_name='School', default='')
    email = models.EmailField(verbose_name='e-mail', default='')
    parent_name = models.CharField(max_length=50, verbose_name='Middle Name', default="")
    contact_number = models.CharField(max_length=12, verbose_name='Contact Number', default='')
    #phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    alternate_contact_number = models.CharField(max_length=12, verbose_name='Alternate Contact Number', default='')
    enquiry_source = models.CharField(max_length=50, verbose_name='Source of Enquiry', default='')
    enquiry_date = models.DateField(default = timezone.now, verbose_name="Date of Enquiry")
    remark = models.CharField(max_length=100, verbose_name ='Remark', blank=True, default="")
    

    def __str__(self):
        return f'{self.name} Data'

    class Meta:
        unique_together = ('name', 'grade', 'contact_number')
        verbose_name = 'Student Data'
        verbose_name_plural = 'Student Data\'s'

