from django.shortcuts import render

from main.models import Experience
from main.models import Education
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from main.forms import ExperienceForm, EducationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required 
from django.core.exceptions import PermissionDenied  
import datetime

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Pearlita Anindya Prameswari",
        "npm": "2506547670",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Information Systems student at Universitas Indonesia, passionate about Product Management and Digital Marketing."
            " Currently a teaching assistant of Business and Technical Communications."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)

# fungsi buat data experience
@login_required(login_url="/login/") 
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New experience has been added successfully!")
        return redirect("main:show_experience")

    context = {
        "name": "Pearlita Anindya Prameswari",
        "form": form,
        "update" : False,
    }
    return render(request, "experience_form.html", context)

# fungsi update data experience
@login_required(login_url="/login/") 
def update_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    experience = Experience.objects.get(id=experience_id) # ambil id experience yang mau di-update dengan .get
    form = ExperienceForm(request.POST or None, instance=experience) # masukin data lama ke form dengan instance

    if request.method == "POST" and form.is_valid():
            form.save()
            messages.success(request, "Experience has been updated successfully!")
            return redirect("main:show_experience")
    
    context = {
        "name": "Pearlita Anindya Prameswari",
        "form": form,
        "update" : True,
    }
    return render(request, "experience_form.html", context)

# fungsi menampilkan experience
def show_experience(request):
    json_response = get_experience_json(request)

    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [experience.object for experience in experiences]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Pearlita Anindya Prameswari",
        "experience_list": experiences,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)

# fungsi ambil data experience dalam format JSON
def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experiences_json = serializers.serialize("json", experiences, use_natural_foreign_keys=True)
    return HttpResponse(experiences_json, content_type="application/json")

# fungsi hapus data experience
@login_required(login_url="/login/") 
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    experience = get_object_or_404(Experience, ek=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience has been deleted succesfully!")
        return redirect("main:show_experience")

    return redirect("main:show_experiece")

# fungsi untuk men-show data education yang di-request
def show_education(request):
    json_response = get_education_json(request)
    educations = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    educations = [education.object for education in educations]
    degree_query = request.GET.get("degree", "").strip()
    
    context = {
        "name": "Pearlita Anindya Prameswari",
        "education_list": educations,
        "degree_query": degree_query,
    }
    return render(request, "education.html", context)

# fungsi untuk buat education
@login_required(login_url="/login/") 
def create_education(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New education has been added successfully!")
        return redirect("main:show_education")

    context = {
        "name": "Pearlita Anindya Prameswari",
        "form": form,
        "update" : False,
    }
    return render(request, "education_form.html", context)

# fungsi ambil data education dalam format JSON
def get_education_json(request):
    degree_query = request.GET.get("degree", "").strip()
    educations = Education.objects.all()

    if degree_query:
        educations = educations.filter(degree__icontains=degree_query)

    educations_json = serializers.serialize("json", educations)
    return HttpResponse(educations_json, content_type="application/json")

#fungsi delete education
@login_required(login_url="/login/") 
def delete_education(request, education_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    education = get_object_or_404(Experience, ek=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Education has been deleted succesfully!")
        return redirect("main:show_education")

    return redirect("main:show_education")

# fungsi update education
@login_required(login_url="/login/") 
def update_education(request, education_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    education = Education.objects.get(id=education_id) # ambil id education yang mau di-update dengan .get
    form = EducationForm(request.POST or None, instance=education) # masukin data lama ke form dengan instance
    
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Education has been updated successfully!")
        return redirect("main:show_education")
        
    context = {
        "name": "Pearlita Anindya Prameswari",
        "form": form,
        "update" : True,
    }
    return render(request, "education_form.html", context)

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Pearlita Anindya Prameswari",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Pearlita Anindya Prameswari",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

# Tanpa cek is_superuser: semua akun yang sudah login boleh memberi star
@login_required(login_url="/login/")
def toggle_star(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")