from django.shortcuts import render, get_object_or_404
from myquora.models import Question, Category

def home(request):
    questions = Question.objects.all()
    categories = Category.objects.all()
    context = {
        'questions': questions,
        'categories': categories
    }
    return render(request, 'myquora/home.htm', context)
    

def question_list(request):
    questions = Question.objects.all()
    categories = Category.objects.all()
    context = {
        'questions': questions,
        'categories': categories
    }
    return render(request, 'myquora/question_list.htm', context)

def question_detail(request, slug):
    question = Question.objects.get(slug=slug)
    categories = Category.objects.all()
    context = {
        'question': question,
        'categories': categories
    }
    return render(request, 'myquora/question_detail.htm', context)

def category_questions(request,slug):
    categories = Category.objects.all()
    category = categories.get(slug=slug)
    questions = category.questions.all()
    context = {
        'categories': categories,
        'category': category,
        'questions':questions
    }
    return render(request, 'myquora/category_questions.htm', context)
    '''
def answer_list(request):
    questions = Question.objects.all()
    categories = Category.objects.all()
    context = {
        'questions': questions,
        'categories': categories
    }
    return render(request, 'myquora/question_list.html', context)
    '''


def ask_question(request):

    if request.method == "POST":
        form = DisplayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("../")

    else:
        form = DisplayForm()    

    return render(request, 'myquora/askquestion.htm', {'form':form})