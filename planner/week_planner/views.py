from django.shortcuts import render
from django.views import View
from . forms import TaskForm
from django.http import HttpResponse
from .models import TaskModel
from django.shortcuts import redirect

# Create your views here.
from django.views import View
from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import TaskModel
from datetime import datetime

class Main(View):
    def get(self, request):
        tasks = TaskModel.objects.all()
        form = TaskForm()
        context = {'form': form, 'tasks': tasks}
        return render(request, 'index.html', context)
    
    def post(self, request):
        form = TaskForm(request.POST)
        
        if form.is_valid():
            task = form.save(commit=False)
            
            # Convert time strings to time objects
            try:
                start_time_str = request.POST.get('start_time')
                end_time_str = request.POST.get('end_time')
                
                if start_time_str:
                    start_time = datetime.strptime(start_time_str, '%H:%M').time()
                    task.start_time = start_time
                
                if end_time_str:
                    end_time = datetime.strptime(end_time_str, '%H:%M').time()
                    task.end_time = end_time
                
                task.save()
                return redirect('/home')
                
            except ValueError as e:
                print(f"Error parsing time: {e}")
                # Handle invalid time format here
                pass
                
        # If form is invalid or time parsing failed
        print("Form errors:", form.errors)
        tasks = TaskModel.objects.all()
        return render(request, 'index.html', {
            'form': form,
            'tasks': tasks,
            'error': 'Invalid form submission'
        })
    



    #delete and edit

class DeleteTask(View):
    def get(self , request , task_id): #get method instead of post because i used a an anchor tag to delete 

        print('IN DELETE')
        task = TaskModel.objects.get(id=task_id)
        task.delete()
        return redirect('/home')
    

class UpdateTask(View):
    def get(self , request , task_id):
        task = TaskModel.objects.get(id=task_id)
        form = TaskForm(instance=task)
        context = {'form': form}

        return render(request , 'update.html' , context)
    
    def post(get , request , task_id):
        task = TaskModel.objects.get(id = task_id)
        form = TaskForm(request.POST , instance=task)

        if form.is_valid():
            task = form.save(commit=False)
        
            start_time_str = request.POST.get('start_time')
            end_time_str = request.POST.get('end_time')
                
            if start_time_str:
                start_time = datetime.strptime(start_time_str, '%H:%M').time()
                task.start_time = start_time
                
            if end_time_str:
                end_time = datetime.strptime(end_time_str, '%H:%M').time()
                task.end_time = end_time
                
                task.save()
            return redirect('/home')
        


class DeleteAll(View):
    def get(self, request):
        all_things_to_do = TaskModel.objects.all()
        all_things_to_do.delete()
        return redirect("/home")