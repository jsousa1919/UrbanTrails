__author__ = 'justin'

from django.contrib.gis import forms

from tags.models import Tag


DISTANCE_CHOICES = (
    (0, 'Any'),
    (1, '1'),
    (5, '5'),
    (10, '10'),
    (50, '50'),
    (100, '100'),
)

class TrailSearchForm(forms.Form):
    tags = forms.ModelChoiceField(Tag, required=False)
    created = forms.TextInput()
    location = forms.GeometryField(required=False, null=True)
    distance = forms.ChoiceField(choices=DISTANCE_CHOICES)
