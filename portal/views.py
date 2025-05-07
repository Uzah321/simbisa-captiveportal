# portal/views.py

from django.shortcuts import render, redirect

def index(request):
    return render(request, 'portal/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Simulate authentication check
        if username == 'user' and password == 'password':
            # Simulate successful login
            return redirect('success')
        else:
            return render(request, 'portal/login.html', {'error': 'Invalid credentials'})
    return render(request, 'portal/login.html')

def success(request):
    return render(request, 'portal/success.html')