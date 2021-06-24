from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render


def Homepage(request):
    return HttpResponseRedirect("https://youtu.be/0DOn2TtlaCk?t=21")

def HtmlViewer(request):
    return render(request,'index.html')