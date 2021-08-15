from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.utils.datastructures import MultiValueDictKeyError
from .models import *


def index(request):
    if request.method == "POST":
        try:
            landingpage = request.POST['landingpage']
        except MultiValueDictKeyError:
            return render(request, "smulithackathon/index.html")
        if request.POST['landingpage'] == "business":
            return render(request, "smulithackathon/business.html")
        if request.POST['landingpage'] == "individual":
            return render(request, "smulithackathon/individual.html")
        
    return render(request, "smulithackathon/index.html")

def information(request):
    if request.method == "POST":
        businesstype = request.POST['businesstype']
        employees = request.POST['employees']
        salary = request.POST['salary']
        profit = request.POST['profit']
        unique_id = get_random_string(length=15)
        f = Business(businesstype=businesstype, employees=employees, salary=salary, profit=profit, encryption=unique_id)
        f.save()
        return render(request, "smulithackathon/information.html",{
            "encryption": unique_id,
            "businesstype": businesstype,
            "employees": employees,
            "salary": int(salary) * int(employees),
            "profit": int(profit),
        })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("smulithackathon:index"))
        else:
            return render(request, "smulithackathon/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "smulithackathon/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("smulithackathon:index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "smulithackathon/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "smulithackathon/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("smulithackathon:index"))
    else:
        return render(request, "smulithackathon/register.html")
