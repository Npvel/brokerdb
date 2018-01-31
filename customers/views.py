from django.shortcuts import render
from .models import Contract

def csvupload(request):

	contract_list = Contract.objects.all()

	return render(request, 'csvupload.html', {'contract_list': contract_list})
