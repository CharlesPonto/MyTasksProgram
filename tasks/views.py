from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, 'tasks/index.html', {
    'tasks': request.session["tasks"] 
    })

def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
        
    return render(request, "tasks/add.html", {
        "form": NewTaskForm
    })

def delete(request, task_index):
    if "tasks" in request.session:
        # Ensure the task index is valid
        if 0 <= task_index < len(request.session["tasks"]):
            # Remove the task at the specified index
            del request.session["tasks"][task_index]
            request.session.modified = True
    
    return HttpResponseRedirect(reverse("tasks:index"))

def edit(request):
    return HttpResponse(
        '<h1 style="align-items:center; justify-content: center; display:flex; height: 60vh;">The "Edit" button functionality will be added soon!</h1>'
    )
