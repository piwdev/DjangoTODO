from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Task, Categories
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import date

# 一覧表示

def task_list(request):
    tasks = Task.objects.all().order_by('-id')
    categories = Categories.objects.all()
    today = date.today().isoformat()
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'categories': categories, 'today': today})

# タスク追加API
@csrf_exempt
def add_task_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        description = data.get('description', '')
        start_date = data.get('start_date')
        until_date = data.get('until_date')
        categories_id = data.get('category_id')
        categories = Categories.objects.filter(id=categories_id).first() if categories_id else None
        task = Task.objects.create(
            title=title,
            description=description,
            start_date=start_date,
            until_date=until_date,
            categories=categories
        )
        return JsonResponse({'success': True, 'task_id': task.id})
    return JsonResponse({'success': False, 'error': 'POSTのみ対応'}, status=400)

# タスク追加フォーム画面

def add_task_input(request):
    categories = Categories.objects.all()
    return render(request, 'tasks/add_task_input.html', {'categories': categories})

def categories_add_input(request):
    return render(request, 'tasks/categories_add_input.html')

@csrf_exempt
def add_categories_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        if not name:
            return JsonResponse({'success': False, 'error': 'カテゴリー名は必須です'}, status=400)
        categories = Categories.objects.create(name=name)
        return JsonResponse({'success': True, 'categories_id': categories.id, 'name': categories.name})
    return JsonResponse({'success': False, 'error': 'POSTのみ対応'}, status=400)

@csrf_exempt
def delete_task_api(request, task_id):
    if request.method == 'POST':
        try:
            task = Task.objects.get(id=task_id)
            task.delete()
            return JsonResponse({'success': True})
        except Task.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'タスクが存在しません'}, status=404)
    return JsonResponse({'success': False, 'error': 'POSTのみ対応'}, status=400)

def edit_task_input(request, task_id):
    task = Task.objects.get(id=task_id)
    categories = Categories.objects.all()
    return render(request, 'tasks/edit_task_input.html', {'task': task, 'categories': categories})

@csrf_exempt
def edit_task_api(request, task_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            task = Task.objects.get(id=task_id)
            task.title = data.get('title', task.title)
            task.description = data.get('description', task.description)
            task.start_date = data.get('start_date', task.start_date)
            task.until_date = data.get('until_date', task.until_date)
            categories_id = data.get('category_id')
            if categories_id:
                categories = Categories.objects.filter(id=categories_id).first()
                task.categories = categories
            task.save()
            return JsonResponse({'success': True})
        except Task.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'タスクが存在しません'}, status=404)
    return JsonResponse({'success': False, 'error': 'POSTのみ対応'}, status=400)
