from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.

class EnterpriseView(View):
	template_name = r'main/enterprise.html'
	def get(self, request):
		return render(request, self.template_name)
