from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

# views base on functions
# def hola_mundo(request):
#     """ home view of app """
#     if request.method == 'POST':
#         print('Hola mundo')
#         return HttpResponse('<h1>Hola mundo</h1>')
    
#     return HttpResponse('<h1>Hola mundo desde GET</h1>')

# def hola_mundo(request):
#     """ home view of app """
#     if request.method == 'POST':
#         print('Hola mundo')
#         return HttpResponse('<h1>Hola mundo</h1>')
    
#     return render(request, 'base.html', {'name': 'Jorge'})

class HomeView(TemplateView):
    template_name = 'home/home.html'
