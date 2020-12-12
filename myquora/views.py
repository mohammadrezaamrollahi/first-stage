from django.shortcuts import render, get_object_or_404
from myquora.models import Question, Category

def home(request):
    questions = Question.objects.all()
    categories = Category.objects.all()
    context = {
        'questions': questions,
        'categories': categories
    }
    return render(request, 'myquora/home_page.html', context)

def question_list(request):
    questions = Question.objects.all()
    categories = Category.objects.all()
    context = {
        'questions': questions,
        'categories': categories
    }
    return render(request, 'myquora/question_list.html', context)

def question_detail(request, slug):
    question = Question.objects.get(slug=slug)
    categories = Category.objects.all()
    context = {
        'question': question,
        'categories': categories
    }
    return render(request, 'myquora/question_detail.html', context)

def category_questions(request, category_id, category_slug):
    categories = Category.objects.all()
    category = categories.get(id=category_id, slug=category_slug)
    questions = category.questions.all()
    context = {
        'categories': categories,
        'category': category,
        'questions': questions
    }
    return render(request, 'myquora/category_questions.html', context)
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