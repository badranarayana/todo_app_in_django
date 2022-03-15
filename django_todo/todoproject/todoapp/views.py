from django.shortcuts import render, HttpResponse, redirect
from .models import Category, Task
from .forms import CreateTaskForm, UpdateTaskForm

# Create your views here.
def todo_list(request):
    tasks = Task.objects.all()
    context = {'todo_list': tasks}
    return render(request, template_name='todoapp/todo_list.html', context=context)


def create_task(request):
    if request.method == 'GET':
        form = CreateTaskForm()
        context = {'form': form}
        return render(request, template_name='todoapp/create_task.html', context=context)

    elif request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['description']
            due_date = form.cleaned_data['due_date']
            category_id = form.cleaned_data['category']
            # category
            category = Category.objects.get(pk=int(category_id))

            # connect to db and save data
            obj = Task(title=title, description=desc, due_date=due_date, category_id=category.id)
            obj.save()

        return redirect(to='todo-list')


def edit_task(request, task_id):
    # get request
    # put
    if request.method == 'GET':
        # first filter tasks by using task id
        task = Task.objects.get(pk=task_id)
        #category = Category.objects.get(pk=task.category_id)

        form_data = {
            'title': task.title,
            'description': task.description,
            'due_date': task.due_date,
            'completed_date': task.completed_date,
            'category': task.category_id
        }

        # this is bounded with db data
        form_with_data = UpdateTaskForm(initial=form_data)

        context = {'form': form_with_data,
                   'id': task.id}
        return render(request, template_name='todoapp/edit_task.html', context=context)

    elif request.method == 'POST':
        post_data = request.POST
        #import pdb;pdb.set_trace()
        if post_data['_method'] == 'PUT':

            form = UpdateTaskForm(request.POST)
            if form.is_valid():
                category_id = form.cleaned_data['category']
                obj = Category.objects.get(pk=int(category_id))

                # update db record
                task = Task.objects.get(pk=task_id)

                task.title = form.cleaned_data['title']
                task.description = form.cleaned_data['description']
                task.due_date = form.cleaned_data['due_date']
                task.completed_date = form.cleaned_data['completed_date']
                task.category_id = obj.id
                # db commit
                task.save()
                return redirect(to='todo-list')
            else:
                context = {'form': form,
                           'id': task_id}
                return render(request, template_name='todoapp/edit_task.html', context=context)


def delete_task(request, task_id):
    # first verify task id it with db
    task = Task.objects.get(pk=task_id)
    task.delete()

    return HttpResponse("Task Deleted Successfully!")








