from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.conf import settings
from core.models import *


@login_required(login_url="/sign-in/?next=/courier/")
def home(request):
    return redirect(reverse('courier:available_jobs'))


@login_required(login_url="/sign-in/?next=/courier/")
def available_jobs_page(request):
    return render(request, "courier/available_jobs.html", {
        "G_M_KEY": settings.G_M_KEY
    })


@login_required(login_url="/sign-in/?next=/courier/")
def available_job_page(request, id):
    job = Job.objects.filter(id=id, status=Job.PROCESSING_STATUS).last()

    if not job:
        return redirect(reverse("courier:available_jobs"))
    return render(request, "courier/available_job.html", {
        "job": job
    })
