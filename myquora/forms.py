from django import forms
from myquora.models import Question , Category , Tag

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ('author' ,'created','updated',)


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        exclude = ('created_time','updated_time' ,)


# class AnswerForm(forms.ModelForm):
#     class Meta:
#         model = Answer
#         pass


