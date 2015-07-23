from django import forms
from chat_journal.models import Post

class EntryForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body',)
