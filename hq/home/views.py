from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.views import View
from django.shortcuts import render_to_response

# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        context={}
        return render(request, "home/index.html", context)

    def post(self, request, *args, **kwargs):
		# print(request.POST)
		# print(request.POST.get("url"))
        form = SubmitUrlForm(request.POST)

        template = "home/index.html"
        return render(request, template)

# def HomeView(request, shortcode=None, *args, **kwargs):
#     template = loader.get_template("home/index.html")
#     return HttpResponse(template.render)
