from django import forms
from .models import comments

class CommentCreationForm(forms.ModelForm):
    class Meta:
        model = comments
        fields = ['text','user','related_blog','parent']
        exclude = ['user','related_blog','parent']