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



