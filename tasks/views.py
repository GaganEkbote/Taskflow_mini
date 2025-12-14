from django.shortcuts import render
from django.http import JsonResponse
from .models import Task   # make sure model name is Task (singular)


# View all tasks
def task_list(request):
    tasks = Task.objects.all().values()
    return JsonResponse(list(tasks), safe=False)


# Create a task
def create_task(request):
    title = request.GET.get('title')

    if title:
        Task.objects.create(title=title)
        return JsonResponse({'message': 'Task created'})

    return JsonResponse({'error': 'Title is required'})


# Mark task as completed
def complete_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.completed = True
        task.save()

        return JsonResponse({'message': 'Task completed'})

    except Task.DoesNotExist:
        return JsonResponse({'error': 'Task not found'})
