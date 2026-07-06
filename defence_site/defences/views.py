from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Defence
from django.forms import ModelForm
from django import forms
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'defences/login.html', {'error': 'Неверное имя пользователя или пароль'})
    return render(request, 'defences/login.html')


def logout_view(request):
    logout(request)
    return redirect('list')


class DefenceForm(ModelForm):
    class Meta:
        model = Defence
        fields = ['title', 'defence_type', 'defence_date', 'status', 'author']
        widgets = {
            'defence_date': forms.DateInput(attrs={'type': 'date'}),
            'title': forms.Textarea(attrs={'rows': 3}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.full_clean()
        if commit:
            instance.save()
        return instance


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