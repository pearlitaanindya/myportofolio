from django.shortcuts import render

from main.models import Experience
from main.models import Education
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from main.forms import ExperienceForm, EducationForm
from django.shortcuts import get_object_or_404, redirect, render

def show_main(request):
    context = {
        "name": "Pearlita Anindya Prameswari",
        "npm": "2506547670",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Information Systems student at Universitas Indonesia, passionate about Product Management and Digital Marketing."
            " Currently a teaching assistant of Business and Technical Communications."
        ),
    }
    return render(request, "index.html", context)

# fungsi buat data experience
def create_experience(request):
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
def update_experience(request, experience_id):
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

    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")

# fungsi hapus data experience
def delete_experience(request, experience_id):
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
def create_education(request):
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
def delete_education(request, education_id):
    education = get_object_or_404(Experience, ek=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Education has been deleted succesfully!")
        return redirect("main:show_education")

    return redirect("main:show_education")

# fungsi update education
def update_education(request, education_id):
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