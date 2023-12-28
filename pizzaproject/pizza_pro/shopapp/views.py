from django.shortcuts import render, redirect
from .models import Item
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse,redirect



def item_list(request):
    items = Item.objects.all()
    return render(request,'index.html',{'items':items})