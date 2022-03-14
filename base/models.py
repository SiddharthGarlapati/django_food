from django.db import models

# Create your models here.

class kid(models.Model):
      kid_name = models.CharField(max_length=50)
      kid_age = models.IntegerField()
      parent_ph_number = models.CharField(max_length=12)
      parent_email_address = models.CharField(max_length=100)

class image(models.Model):

    food_choices = (('veg','veg'),('fruit','fruit'),('Grain','Grain'),('Protein','Protein'),('Dairy','Dairy'),('Confectionery','Confectionery'),('Unknown','Unknown'))
    kid = models.ForeignKey(kid,on_delete = models.CASCADE)
    image_url = models.URLField(max_length=200)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)
    is_approved = models.BooleanField()
    food_group = models.CharField(max_length=100, choices = food_choices)




