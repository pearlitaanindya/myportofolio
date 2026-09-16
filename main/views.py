from django.shortcuts import render

from main.models import Experience
from main.models import Education
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from main.forms import ExperienceForm
from django.shortcuts import get_object_or_404, redirect, render

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New experience has been added successfully!")
        return redirect("main:show_experience")

    context = {
        "name": "Pearlita Anindya Prameswari",
        "form": form,
    }
    return render(request, "experience_form.html", context)



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

# fungsi untuk men-show data education yang di-request
def show_education(request):
    context = {
        "name" : "Pearlita Anindya Prameswari", 
        "education_list" : Education.objects.all(),
    }
    return render(request, "education.html", context)

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, ek=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience has been deleted succesfully!")
        return redirect("main:show_experience")

    return redirect("main:show_experiece")