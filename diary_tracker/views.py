from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from diary_tracker.forms import DiaryRecordForm
from diary_tracker.models import DiaryRecord
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.contrib.auth.decorators import login_required

# Create your views here.
def show_tracker(request):
    context = {
    }
    return render(request, "diary_tracker.html", context)

def create_diary(request):
    form = DiaryRecordForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('diary_tracker:show_tracker'))

    context = {'form': form}
    return render(request, "create_diary.html", context)

def modify_diary(request, id):
    # Get data berdasarkan ID
    transaction = DiaryRecord.objects.get(pk = id)

    # Set instance pada form dengan data dari transaction
    form = DiaryRecordForm(request.POST or None, instance=transaction)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('diary_tracker:show_tracker'))

    context = {'form': form}
    return render(request, "modify_diary.html", context)

def delete_diary(request, id):
    # Get data berdasarkan ID
    transaction = DiaryRecord.objects.get(pk = id)
    # Hapus data
    transaction.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('diary_tracker:show_tracker'))

@csrf_exempt
def create_diary_ajax(request):  
# create object of form
    form = DiaryRecordForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        data = DiaryRecord.objects.last()

    # parsing the form data into json
    result = {
        'date':data.date,
        'description':data.description,
        'id': data.id,
    }
    return JsonResponse(result)

    context = {'form': form}
    return render(request, "create_diary.html", context)

def show_xml(request):
    data = DiaryRecord.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = DiaryRecord.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = DiaryRecord.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = DiaryRecord.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")