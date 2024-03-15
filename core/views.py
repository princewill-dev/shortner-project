from django.shortcuts import redirect

# redirect to home page
def home_view(request):
    return redirect('https://sht.cx/comingsoon/')