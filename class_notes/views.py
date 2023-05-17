from django.shortcuts import render
from class_notes.models import Note
from django.http import HttpResponseRedirect
from class_notes.forms import NoteForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers

def show_note(request):
    note = Note.objects.all()
    context = {
        'class_notes': note,
        
    }

    return render(request, "note.html", context)

def create_note(request):
    form = NoteForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('class_notes:show_note'))

    context = {'form': form}
    return render(request, "create_note.html", context)

def show_xml(request):
    data = Note.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Note.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request):
    data = Note.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request):
    data = Note.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def modify_note(request, id):
    # Get data berdasarkan ID
    note = Note.objects.get(pk = id)

    # Set instance pada form dengan data dari transaction
    form = NoteForm(request.POST or None, instance=note)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('class_notes:show_note'))

    context = {'form': form}
    return render(request, "modify_note.html", context)

def delete_note(request, id):
    # Get data berdasarkan ID
    note = Note.objects.get(pk = id)
   
    note.delete()
    
    return HttpResponseRedirect(reverse('class_notes:show_note'))


