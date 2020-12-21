from django import forms
from myquora.models import Question , Category

# class QuestionForm(forms.ModelForm):
#     class Meta:
#         model = Question
#         fields = ["question_title", "question_text", "question_category"]



# class QuestionForm(forms.ModelForm):
#     title = forms.CharField(max_length=150, required=True)
#     body = forms.CharField(max_length=5000, required=False)

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_title', 'question_text', 'category','tag_question')

