from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Studentdata
from datetime import datetime


# Create your views here.
class MainView(TemplateView):
	template_name = 'schoolinfo/studentinfo.html'
    
	def get(request):
		form = Mainform()
		return render(request,template_name)

	def post(self, request):
		form = Mainform(request.POST)
		if form.is_valid():
			text = form.cleaned_data['fname']
			number = form.cleaned_data['id']

		args = Studentdata.objects.filter( first_name =text)
		return render(request,self.template_name, args)
	

def urlsearch(request,studentid):
	args = Studentdata.objects.get(id= studentid)
	return render(request,'schoolinfo/urlbasedtemplate.html',{'args':args})