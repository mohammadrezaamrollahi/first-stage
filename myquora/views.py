from django.shortcuts import render, get_object_or_404 ,redirect
from myquora.models import Question, Category
from .forms import QuestionForm ,AnswerForm
from django.template.defaultfilters import slugify
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView





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

class QuestionDetailView(DetailView):
    model = Question
    template_name = 'myquora/question_detail.htm'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        question_menu = Question.objects.all()
        the_question = get_object_or_404(Question, id=self.kwargs['pk'])
        total_likes = the_question.get_total_likes()
        liked = False
        if the_question.likes.filter(id=self.request.user.id).exists():
            liked = True
        context = super(QuestionDetailView, self).get_context_data(*args, **kwargs)
        context["categories"] = category_menu
        context["questions"] = question_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

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
            return redirect("/")

    else:
        form = QuestionForm()    

    return render(request, 'myquora/add_question.htm', {'form':form})  


def like_view(request, pk):
    question = get_object_or_404(Question, id=request.POST.get('question_id'))
    liked = False
    if question.likes.filter(id=request.user.id).exists():
        question.likes.remove(request.user)
        liked = False
    else:
        question.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse("myquora:question-detail", args=[str(pk)]))

def create_answer(request, pk):
    question = get_object_or_404(Question, id=pk)
    new_answer = None
    form=AnswerForm()
    if request.method == "POST":
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            new_answer = form.save(commit=False)
            new_answer.question = Question.objects.get(id=pk)
            new_answer.user = request.user
            new_answer.save()
            return redirect("/")
    else:
        form = AnswerForm
    return render(request,"myquora/create_answer.htm", {"questions": question,"new_answer": new_answer,"form": form,},)
