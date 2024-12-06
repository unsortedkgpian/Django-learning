from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class DanjoVarity(models.Model):
    DJANGO_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELACHI')
    ]    
    name= models.CharField(max_length=100)
    image =models.ImageField(upload_to='atomicapp/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=DJANGO_TYPE_CHOICE)
    description = models.TextField(default='')
    
    
    def __str__(self) :
        return self.name


# one to many
class atomReviews(models.Model):
    atom = models.ForeignKey(DanjoVarity , on_delete=models.CASCADE, related_name='rewies')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment=models.IntegerField()
    date_added = models.DateTimeField(default= timezone.now)

    def __str__(self) :
        return f'{self.user.username} review for {self.chai.name}'

## Many to Many

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(DanjoVarity, related_name='stores')

    def __str__(self) :
        return self.name
    
    
#One to one
class AtomCertification(models.Model):
    atom = models.OneToOneField(DanjoVarity, on_delete=models.CASCADE, related_name='certificate')
    certicate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_untill = models.DateTimeField()
    
    def __str__(self) :
        return self.name.atom