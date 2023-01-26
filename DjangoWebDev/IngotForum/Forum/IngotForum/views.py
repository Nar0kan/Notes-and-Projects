from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, IngNote

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        ingnotes = IngNote.objects.all().order_by("-create_time")
        return render(request, 'home.html', {"ingnotes": ingnotes})
    else:
        return render(request, 'home.html')


def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
    else:
        messages.success(request, ("You must log in to see this."))
        return render(request, 'home.html')

    return render(request, 'profile_list.html', {'profiles': profiles})


def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        ingnotes = IngNote.objects.filter(user_id=pk).order_by("-create_time")

        if request.method == "POST":
            request_user = request.user.profile
            action = request.POST['follow']

            if action == "unfollow":
                request_user.follows.remove(profile)
            elif action == "follow":
                request_user.follows.add(profile)
            
            request_user.save()

        return render(request, "profile.html", {"profile": profile, "ingnotes": ingnotes})
    else:
        messages.success(request, ('You must be logged in to see this profile information.'))
        return render(request, 'home.html')