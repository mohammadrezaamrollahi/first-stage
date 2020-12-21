from django.shortcuts import render, get_object_or_404
from myquora.models import Question, Category
from .forms import QuestionForm
from django.template.defaultfilters import slugify


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
    question=get_object_or_404(Question, slug=slug)
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

# def add_question(request):
#     if request.method == 'POST':
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             question = Question(question_title=cd['title'])
#             if cd['slug']:
#                 question.slug = slugify(cd['slug'])
#             else:
#                 question.slug = slugify(cd['title'])
#             question.save()
#             return redirect('myquora:question-list')
#     else:
#         form = QuestionForm()
#         questions = Question.objects.all()
#         categories = Category.objects.all()
#         return render(request, 'myquora/add_question.htm', {'form': form, 'categories': categories})
def add_question(request):

    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = QuestionForm()    

    return render(request, 'myquora/add_question.htm', {'form':form})    

# def add_question(request):
#     if request.method == 'POST':
#         pass
#     else:
#         form = QuestionForm()
#         categories = Category.objects.all()
#         return render(request, 'myquora/add_question.htm', {'form': form, 'categories': categories})