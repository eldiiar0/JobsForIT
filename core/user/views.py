from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm


def sign_up(request):
    form = SignUpForm()
    if request.method == 'GET':
        context = {'form': form}
        return render(request, 'user/sign-up.html', context)
    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('main')
    else:
        print('Form is not valid')
        messages.error(request, 'Error Processing Your Request')
        context = {'form': form}
        return render(request, 'sign-up.html.html', context)

    return render(request, 'sign-up.html.html', {})
