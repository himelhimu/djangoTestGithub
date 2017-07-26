from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import Http404, HttpResponseRedirect, HttpResponse

from .models import Question, Choice


# Create your views here.

def index(request):
    question_list = Question.objects.all()
    template = loader.get_template("polls/index.html")
    response = ",".join([question.question_text for question in question_list])
    return render(request, "polls/index.html", {"question_list": question_list})


def details(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question Does not exists")
    return render(request, "polls/details.html", {"question": question})


def results(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/details.html", {"question": question,
                                                      "error_message": "You didn't select a choice ", })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))


# Using djangos get_object_or_404
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
