from django.shortcuts import render
# from django.contrib.auth.models import User
from hierarchical.models import File


def show_files(request):
    files = File.objects.all()
    return render(request, "files.html", {'files': files})
