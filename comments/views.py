from django.shortcuts import render
from django.views.generic import TemplateView,DetailView,View
from django.views.generic.edit import FormMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Blog,comments
from user.models import User
from .forms import CommentCreationForm

class BlogView(FormMixin,DetailView):
    template_name = 'comments/test.html'
    context_object_name = 'blog'
    form_class = CommentCreationForm

    def get_object(self):
        return get_object_or_404(Blog,pk=self.kwargs.get('pk'))

    def get_context_data(self, *args, **kwargs):
        context = super(BlogView, self).get_context_data(*args, **kwargs)
        context['usercomments'] = comments.objects.filter(related_blog=self.object)
        context['form'] = self.get_form()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self,form):
        form.instance.user = User.objects.get(pk = self.request.user.pk)
        form.instance.related_blog = self.object
        form.save()

        return super(BlogView, self).form_valid(form)        
    
    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', '/')
    
class Reply(FormMixin,View):
    form_class = CommentCreationForm
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self,form):
        form.instance.user = User.objects.get(id = self.request.user.id)
        form.instance.related_blog = get_object_or_404(Blog,id = self.kwargs.get('blog_id'))
        form.instance.parent = get_object_or_404(comments,id = self.kwargs.get('comment_id'))
        form.save()

        return super(Reply, self).form_valid(form)
    
    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', '/')
