from django.shortcuts import render, redirect
from .models import Todo
from .forms import CreateTodoForm
from django.contrib import messages


def index_page_view(request):
    return redirect('/todos')

def todo_page_view(request):
    #if request.user and request.user.is_authenticated:
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



def todo_details_view(request, pk):
    todos = Todo.objects.get(id=pk)
    return render(request, 'todos/todo-details.html', {'todos': todos})

def delete_todo_page_view(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
        todo.delete()
        return redirect('/todos')    
    except Todo.DoesNotExist:
        #return redirect('/todos')
        error = 'Todo not Found'
        messages.error(request, message=error)
        return redirect('/todos')


def basket_page_view(request,):
    if request.user.is_authenticated:
        if request.method == 'GET':
            items = Todo.objects.filter(owner_id=request.user.id)
            return render(request, 'todos/basket.html', {'items': items})
    else:
        return redirect('/auth/login')

def add_todo_to_basket_view(request, pk):
    if request.user.is_authenticated:
        basket_item = BasketItem(todo_id=pk, owner_id=request.user.id, amount=1)
        basket_item.save()
        return redirect('/basket/')
    else:
        return redirect('/auth/login/')


def delete_from_basket_view(request, pk):
    order = BasketItem.objects.get(id=pk)
    if request.user.is_authenticated and request.user.id == order.owner.id:
        order.delete()
        return redirect('/basket/')
    else:
        return redirect('/')