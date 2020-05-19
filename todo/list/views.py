from django.shortcuts import render
from .models import Task

# Create your views here.


def task_list(request):
    tasks = Task.objects.all()
    statuses = ['Ожидает выполнения', 'В процессе выполнения', 'Выполнена']
    wait = tasks.filter(status=statuses[0])
    draft = tasks.filter(status=statuses[1])
    complete = tasks.filter(status=statuses[2])

    return render(request, 'list/list.html', {'tasks': tasks, 'wait': wait,
                                              'draft': draft, 'complete': complete})
