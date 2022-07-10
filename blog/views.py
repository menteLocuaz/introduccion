from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import View,UpdateView,DeleteView
from .form import PostCreateForm
from .models import Post
# Create your views here.
class BlogListView(View):
    def get(self,req,*args,**kwargs):
        posts=Post.objects.all()
        context={
            'posts':posts
        }
        return render(req,'blog_list_index.html',context)

class BlogCreateViews(View):
    def get(self,req,*args,**kwargs):
        form=PostCreateForm()
        context={
            'form':form
        }
        return render(req,'blog_create.html',context)

    def post(self,req,*args,**kwargs):
        if req.method == "POST":
            form=PostCreateForm(req.POST)
            if form.is_valid():
                title=form.cleaned_data.get('title')
                content=form.cleaned_data.get('content')

                p,created=Post.objects.get_or_create(title=title,content=content)
                p.save()
                return redirect('blog:home')

        context={
        }
        return render(req,'blog_create.html',context)

class BlogDetailView(View):
    def get(self,req,pk,*args,**kwargs):
        post=get_object_or_404(Post,pk=pk)
        context={
            'post':post
        }
        return render(req,'blog_datail.html',context)

class BlogUpdateView(UpdateView):
    model=Post
    fields=['title','content']
    template_name='blog_update.html'

    def get_success_url(self):
        pk=self.kwargs['pk']
        return reverse_lazy('blog:detail',kwargs={'pk':pk})

class BlogDeleteView(DeleteView):
    model=Post
    template_name='blog_delete.html'
    success_url=reverse_lazy('blog:home')
