from django.shortcuts import render
from .models import Task

# Create your views here.


def task_list(request):
    tasks = Task.objects.values()
    statuses = ['Ожидает выполнения', 'В процессе выполнения', 'Выполнена']
    draft, wait, complete = [], [], []
    for task in tasks:
        if task['status'] == statuses[0]:
            wait.append(task)
        elif task['status'] == statuses[1]:
            draft.append(task)
        elif task['status'] == statuses[2]:
            complete.append(task)

    return render(request, 'list/list.html', {'tasks': tasks, 'wait': wait,
                                              'draft': draft, 'complete': complete})
