from django import forms
from myquora.models import Question , Category , Tag , Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ('created','updated',"likes",)


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ("content",)


# class TagForm(forms.ModelForm):
#     class Meta:
#         model = Tag
#         exclude = ('created_time','updated_time' ,)





