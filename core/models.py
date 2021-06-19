from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from phone_field import PhoneField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='avatar-5.jpg', null=True)
    phone = models.CharField(max_length=13, null=True)
    GENDER = (('Male', 'Male'),('Female', 'Female'),('Other', 'Other'))
    gender = models.CharField(max_length=10, choices=GENDER, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

class MeetLink(models.Model):
    DAYS = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday','Sunday')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100, null=True)
    meet_link = models.CharField(max_length=100, null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    day = models.CharField(max_length=15, choices=DAYS, null=True)

    def __str__(self):
        return self.course_name