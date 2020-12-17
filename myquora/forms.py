from django import forms
from myquora.models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'text', 'category')