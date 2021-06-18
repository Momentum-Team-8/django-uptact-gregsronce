from django.forms import ModelForm, Textarea
from django.db import models
from django.db.models import fields
from .models import Contact, Note


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'address_1',
            'address_2',
            'city',
            'state',
            'zip_code',
            'phone_number',
            'email',
            'birthday',
        ]

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = [
            'note', 
        ]

