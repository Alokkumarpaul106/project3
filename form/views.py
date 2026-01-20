from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm

def user_form_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  # Save data to DB
            messages.success(request, 'Form submitted successfully!')
            return redirect('user_form')
    else:
        form = UserForm()
    
    return render(request, 'form/index.html', {'form': form})
