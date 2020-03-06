from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from hierarchical.models import File
from hierarchical.forms import TreeForm


def show_files(request):
    files = File.objects.all()
    return render(request, "files.html", {'files': files})


def file_view(request):
    html = "form_view.html"

    if request.method == "POST":
        form = TreeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            File.objects.create(
                name=data['name'],
                parent=data['parent']
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = TreeForm()

    return render(request, html, {'form': form})


# def login_view(request):
#     html = "login.html"

#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             user = authenticate(username=data['username'], password=data['password'])
#             # login(request, user)
#             if user is not None:
#                 login(request, user)
#                 # Where we want to go next after logging in correctly
#                 return HttpResponseRedirect(request.GET.get('next', '/'))
#     else:
#         form = LoginForm()
#     return render(request, html, {'form': form})


# def logout_view(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('homepage'))


# def signup_view(request):
#     html = "signup.html"

#     if request.method == "POST":
#         form = SignupForm(request.POST)

#         if form.is_valid():
#             data = form.cleaned_data

#             user = User.objects.create_user(
#                 data['username'],
#                 data['password'],
#             )

#             login(request, user)
#             NewUser.objects.create(
#                 username=data['username'],
#                 password=data['password'],
#                 user=user
#             )

#             return HttpResponseRedirect(reverse("homepage"))

#     form = SignupForm()
#     return render(request, html, {'form': form})
