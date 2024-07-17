from django.shortcuts import render

# Create your views here.
def Home(request):
    user = request.user
    return render(request, 'main/home.html', {'user': user})