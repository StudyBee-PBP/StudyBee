from time import timezone
from django.shortcuts import get_object_or_404, render, redirect
from study_bee.models import StudyPlan
from django.http import HttpResponse, HttpResponseRedirect
from study_bee.forms import StudyPlanForm
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.utils import timezone
from django.core import serializers




# Create your views here.



def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('study_bee:login')

    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("study_bee:show_planner")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('study_bee:login'))
    response.delete_cookie('last_login')
    return response


@login_required(login_url='/study_bee/login/')
def show_planner(request):
    if request.method == 'POST':
        form = StudyPlanForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudyPlanForm()
    now = timezone.now()
    study_plans = StudyPlan.objects.all().order_by('-date')
    return render(request, 'planner.html', {'form': form, 'study_plans': study_plans, 'now': now})

def add_plan(request):
    if request.method == 'POST':
        form = StudyPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('study_bee:planner'))
    else:
        form = StudyPlanForm()
    return render(request, 'add_plan.html', {'form': form})


def edit_plan(request, plan_id):
    study_plan = get_object_or_404(StudyPlan, pk=plan_id)

    if request.method == 'POST':
        form = StudyPlanForm(request.POST, instance=study_plan)
        if form.is_valid():
            form.save()
            return redirect('study_bee:planner')
    else:
        form = StudyPlanForm(instance=study_plan)

    return render(request, 'edit_plan.html', {'form': form, 'study_plan': study_plan})



def delete_plan(request, plan_id):
    plan = get_object_or_404(StudyPlan, pk=plan_id)
    if request.method == 'POST':
        plan.delete()
        return redirect('study_bee:planner')
    return render(request, 'delete_plan.html', {'plan': plan})


def show_json(request):
    data = StudyPlan.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = StudyPlan.objects.filter(pk=id)

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
