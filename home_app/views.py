from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

    

class MyHomeView(TemplateView):

    def get(self, request):
        return render(request, 'home_app/home.html')