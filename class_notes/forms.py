from django.forms import ModelForm
from class_notes.models import Note

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ["title", "subject",  "content"]
