from multiprocessing import get_context
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.views.generic.edit import DeleteView




from mainapp.forms import AddNewsForm, PaginateForm
from mainapp.models import News
from mainapp.utils import DataMixin

class NewsHome(ListView, DataMixin):
    paginate_by= 10
    model = News
    template_name = 'mainapp/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        if self.request.GET.get("paginate_by"):
            self.paginate_by = self.request.GET.get("paginate_by")
        context = super().get_context_data(**kwargs)
        c_def = self.get_all_context(title="Главная страница")
        context['form'] = PaginateForm()
        return dict(list(context.items()) + list(c_def.items()))
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class AddPage(CreateView, DataMixin):
    form_class = AddNewsForm
    template_name = 'mainapp/addpage.html'
    success_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_all_context(title="Добавление статьи")
        return dict(list(context.items()) + list(c_def.items()))

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class ShowPost(DetailView, DataMixin):
    model = News
    template_name = 'mainapp/post.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_all_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')