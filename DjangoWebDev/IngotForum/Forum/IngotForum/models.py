from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class IngNote(models.Model):
    user = models.ForeignKey(User, related_name="ingnote", on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=1000)
    create_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return (f"{self.user} | {self.create_time:%Y-%m-%d %H:%M} | {self.body}")


# Create a User profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self",
        related_name="followed_by",
        symmetrical=False,
        blank=True)

    date_modified = models.DateTimeField(User, auto_now=True)

    def __str__(self) -> str:
        return self.user.username


# Create Profile when user Signs up
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        
        # User must follow himself
        user_profile.follows.set([instance.profile.id])
        user_profile.save()

#post_save.connect(create_profile, sender=User)