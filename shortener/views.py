from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect

# connection test
def test_view(request):
    return JsonResponse({'message': 'Hello, world!'})

# redirect to home page
def redirect_view(request):
    return redirect('https://sht.cx')
