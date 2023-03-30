from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'GET':
        form = UserCreationForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'register.html', context)
