from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
  topic=models.CharField(max_length=250)
  creator=models.ForeignKey(User,on_delete=models.CASCADE,related_name="creator")
  description=models.TextField(blank=True,null=True)
  location=models.CharField(max_length=200)
  date_and_time=models.DateTimeField(auto_now=True)
  #attendees=models.ManyToManyField(User,related_name="attendees",through='attendees')
  def __str__(self):
    return self.topic
