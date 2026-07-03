from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Defence
from django.forms import ModelForm
from django import forms

class DefenceForm(ModelForm):
    class Meta:
        model = Defence
        fields = ['title', 'defence_type', 'defence_date', 'status', 'author']
        widgets = {
            'defence_date': forms.DateInput(attrs={'type': 'date'}),
            'title': forms.Textarea(attrs={'rows': 3}),
        }

def list_view(request):
    defences = Defence.objects.all()
    return render(request, 'defences/list.html', {'defences': defences})

def create_view(request):
    if request.method == 'POST':
        form = DefenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = DefenceForm()
    return render(request, 'defences/form.html', {'form': form, 'title': 'Добавить защиту'})

def edit_view(request, pk):
    defence = get_object_or_404(Defence, pk=pk)
    if request.method == 'POST':
        form = DefenceForm(request.POST, instance=defence)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = DefenceForm(instance=defence)
    return render(request, 'defences/form.html', {'form': form, 'title': 'Редактировать защиту'})

def delete_view(request, pk):
    defence = get_object_or_404(Defence, pk=pk)
    if request.method == 'POST':
        defence.delete()
        return redirect('list')
    return render(request, 'defences/confirm_delete.html', {'defence': defence})

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list')
    else:
        form = AuthenticationForm()
    return render(request, 'defences/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('list')