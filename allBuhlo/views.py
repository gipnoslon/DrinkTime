from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Отображение главной страницы
def index(reqest):
	Alcholist = Alcohol.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
	paginator = Paginator(Alcholist,2,orphans=1)
	
	page = reqest.GET.get('page')

	try:
		alch = paginator.page(page)
	except PageNotAnInteger:
		alch = paginator.page(1)
	except EmptyPage:
		alch = paginator.page(paginator.num_pages)

	return render(reqest, 'allBuhlo/Buhlo_list.html', {'alch':alch})


#Полное отобрадение эелемента
def buhlo_detail(reqest, pk,name):
	detail = get_object_or_404(Alcohol,pk=pk)
	ingrs = IngLitr.objects.filter(alcohol=pk)
	
	return render(reqest, 'allBuhlo/buhlo_detail.html',{'detail' : detail,'ingrs': ingrs})


#Отображение поиска по ключу
def choicekey(reqest):
	querty = dict(reqest.GET)["choice"]
	#Фильтровка по ключу уникальных элементов
	Alcholist = Alcohol.objects.filter(ingredients__in=IngLitr.objects.filter(ingname_id__in=querty)).order_by('publish_date').distinct()
	paginator = Paginator(Alcholist,2,orphans=1)
	
	page = reqest.GET.get('page')

	try:
		alch = paginator.page(page)
	except PageNotAnInteger:
		alch = paginator.page(1)
	except EmptyPage:
		alch = paginator.page(paginator.num_pages)
    
	return render(reqest, 'allBuhlo/searchonkeyresult.html', {'alch': alch})



#Поиск по имени
def choicename(reqest):
	quertyname = dict(reqest.GET)["choicenames"]
	#Фильтровка по ключу уникальных элементов
	FilterOnName = Alcohol.objects.filter(title__iexact=quertyname).order_by('publish_date').distinct()
	paginator = Paginator(FilterOnName,2,orphans=1)
	
	return HttpResponse(quertyname)

	page = reqest.GET.get('page')

	try:
		alchfilter = paginator.page(page)
	except PageNotAnInteger:
		alchfilter = paginator.page(1)
	except EmptyPage:
		alchfilter = paginator.page(paginator.num_pages)


    
	#return render(reqest, 'allBuhlo/searchonnameresult.html', {'alch': alchfilter}) 

