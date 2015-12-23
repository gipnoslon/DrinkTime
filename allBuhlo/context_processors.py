from .models import *

def valuesForNameSearch(request):
	valuesForNameSearchs = Alcohol.objects.values()
	return {"choicename" : valuesForNameSearchs}

def valuesForKeySearch(request):
	valuesForKeySearchs = Ingridient.objects.values()
	return {"choices" : valuesForKeySearchs}