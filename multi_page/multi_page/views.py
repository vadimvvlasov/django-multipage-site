from django.shortcuts import render
from . import this_is_machine_learning_model

def home(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def result(request):
    user_input = request.GET['user_input']
    user_input = this_is_machine_learning_model.multiplier(user_input)
    return render(request, 'result.html', {'home_input': user_input})
