from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Pearlita Anindya Prameswari",
        "npm": "2506547670",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Information Systems student at Universitas Indonesia, passionate about Product Management and Digital Marketing."
            "Currently a teaching assistant of Business and Technical Communications."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Pearlita Anindya Prameswari",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)