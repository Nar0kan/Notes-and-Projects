from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    is_organisor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)
    position = models.CharField(max_length=100, default="employee", null=True, blank=True)
    phone_number = models.CharField(max_length=100, default="unknown", null=True, blank=True)
    photo = models.ImageField(verbose_name="Photo", null=True, blank=True, upload_to="images/agents")


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Lead(models.Model):
    first_name = models.CharField(max_length=28)
    last_name = models.CharField(max_length=28)
    age = models.IntegerField(default=0)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    photo = models.ImageField(verbose_name="Photo", null=True, blank=True, upload_to="images/leads")

    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    agent = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL)    # Every lead has an agent
    category = models.ForeignKey("Category", related_name="lead_cat", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)             # Agent == User(AbstractUser)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE) # Organisation == UserProfile == User(AbstractUser)

    def __str__(self):
        return self.user.email


class Category(models.Model):
    name = models.CharField(max_length=50)
    organisation = models.ForeignKey(UserProfile, on_delete = models.CASCADE)

    def __str__(self):
        return self.name


class Document(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    is_secret = models.BooleanField(default=False)
    file = models.FileField(verbose_name=title, null=False, blank=False, upload_to="media/")
    date_added = models.DateTimeField(auto_now_add=True)

    lead = models.ForeignKey("Lead", null=False, blank=False, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


def postUserCreatedSignal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(postUserCreatedSignal, sender=User)


@receiver(post_save, sender=UserProfile)
def create_categories(sender, instance, created, **kwargs):
    if created:
        category_names = ['Unassigned', 'Contacted', 'Converted', 'Unconverted']
        for name in category_names:
            Category.objects.create(name=name, organisation=instance)