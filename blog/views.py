from django.shortcuts import render
from django.views import View

# Create your views here.
class BlogListView(View):
    def get(self,req,*args,**kwargs):
        context={
        }
        return render(req,'blog_list_index.html',context)