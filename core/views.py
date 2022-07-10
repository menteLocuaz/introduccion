from django.shortcuts import render
from django.views.generic import View

class HomeViews(View):
    def get(self,req,*args,**kwargs):
        context={

        }
        return render(req,'index.html',context)