from django import forms
from myquora.models import Question , Category ,Answer ,Tag


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["tag_name"]

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            "question_title",
            "question_text",
            "category",
            "question_tag",
        ]


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ("content",)







