from django.shortcuts import render, redirect
from .models import Todo
from .forms import CreateTodoForm


def index_page(request):
    if request.method == 'GET':
        form = CreateTodoForm()
        todos = Todo.objects.all()
        return render(request, 'todos/index.html', {'todos': todos, 'form': form})
    if request.method == 'POST':
        print(request.POST)
        #title = request.POST.get('title', '')
        #description = request.POST.get('description', '')
        #due_date = request.POST.get('due_date', '')
        #status = request.POST.get('status', '')

        form = CreateTodoForm(request.POST)

        if form.is_valid():
            title = form.data.get('title')
            description = form.data.get('description')
            due_date = form.data.get('due_date')
            enabled = form.data.get('status')
            status = False
            if enabled == 'on':
                status = True
            todo = Todo(title=title, description=description, due_date=due_date, status=status)
            todo.save()
        todos = Todo.objects.all()
        return render(request, 'todos/index.html', {'todos': todos, 'form': form})


def todo_details(request, pk):
    todos = Todo.objects.get(id=pk)
    return render(request, 'todos/todo-details.html', {'todos': todos})

def delete_todo(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
        todo.delete()
        return redirect('/todos')
    except Todo.DoesNotExist:
        return redirect('/todos')
        #error = 'Todo not Found'
        #form = CreateTodoForm()
        #todos = Todo.objects.all()
        #return render(request, 'todos/index.html', {'todos': todos, 'form': form, 'error': error})