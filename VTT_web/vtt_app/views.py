
from django.shortcuts import render, redirect
from .models import MedicalImage, TestResult
from .forms import MedicalImageForm, TestResultForm


def home(request):
    return render(request, 'home.html')


def upload_image(request):
    if request.method == 'POST':
        form = MedicalImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = MedicalImageForm()
    return render(request, 'upload_image.html', {'form': form})

def image_list(request):
    images = MedicalImage.objects.all()
    return render(request, 'image_list.html', {'images': images})

def record_result(request, image_id):
    image = MedicalImage.objects.get(id=image_id)
    if request.method == 'POST':
        form = TestResultForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.image = image
            result.save()
            return redirect('image_list')
    else:
        form = TestResultForm()
    return render(request, 'record_result.html', {'form': form, 'image': image})