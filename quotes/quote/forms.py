from django import forms
from .models import Tag,Quote

class QuoteForm(forms.ModelForm):
    # tags=forms.MultipleChoiceField(Tag.objects.all())
    class Meta:
        model=Quote
        fields=['text','author','tags']