from django.shortcuts import render
def show_note(request):
    return render(request, "note.html")


