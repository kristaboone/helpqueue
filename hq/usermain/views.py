from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.views import View

# Create your views here.
class MainView(View):
    def get(self, request, *args, **kwargs):
        page = self.get_page(request)
        return render(request, page)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        page = self.get_page(request)
        return render(request, template)

    def get_page(self, request):
        grouplist = request.user.groups.all()

        if len(grouplist) > 0:
            group = str(grouplist[0])
            # check user type and set page to appropriate user
            if group == "Instructor":
                page = "instructor_main.html"
            else:
                page = "student_main.html"
        else:
            raise Exception('You are not part of any groups!')
        return page
