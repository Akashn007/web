from django.shortcuts import render, redirect, get_object_or_404
from .models import Study
from .forms import StudyForm
from django.contrib import messages

# List all studies
def study_list(request):
    studies = Study.objects.all()
    return render(request, 'studies/study_list.html', {'studies': studies})

# Add a new study
def add_study(request):
    if request.method == 'POST':
        form = StudyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Study added successfully.")
            return redirect('study_list')
    else:
        form = StudyForm()
    return render(request, 'studies/add_study.html', {'form': form})

# View details of a single study
def view_study(request, pk):
    study = get_object_or_404(Study, pk=pk)
    return render(request, 'studies/view_study.html', {'study': study})

# Edit an existing study
def edit_study(request, pk):
    study = get_object_or_404(Study, pk=pk)
    if request.method == 'POST':
        form = StudyForm(request.POST, instance=study)
        if form.is_valid():
            form.save()
            messages.success(request, "Study updated successfully.")
            return redirect('study_list')
    else:
        form = StudyForm(instance=study)
    return render(request, 'studies/edit_study.html', {'form': form})

# Delete a study
def delete_study(request, pk):
    study = get_object_or_404(Study, pk=pk)
    study.delete()
    messages.success(request, "Study deleted successfully.")
    return redirect('study_list')

def attachments(request,pk):
    Study=get_object_or_404(Study,pk=pk)
    if request.method=="POST":
        form = StudyForm(request.POST,instance=Study)
        form.save()
        messages.success(request,"attachment succesful")
        return redirect(study_list)
    else:
        form = StudyForm(instance=Study)
        return render(request,'studies/add_study.html',{'form':form,'study':Study})
    
