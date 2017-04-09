from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.views import View


# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        context={}
        return render(request, "homepage.html", context)

    def post(self, request, *args, **kwargs):
		# print(request.POST)
		# print(request.POST.get("url"))
        form = SubmitUrlForm(request.POST)
        template = "homepage.html"
        return render(request, template)

def login_form(request):
    return render(request, 'login.html')

def login(request):
    if 'q' in request.GET:
            message = 'You submitted a thing'
            request.GET['q']
    else:
            message = 'Form empty.'
    return HttpResponse(message)
