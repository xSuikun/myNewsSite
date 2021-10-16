from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.contrib import messages

from .forms import NewsForm, UserRegisterForm, UserLoginForm, ContactForm
from .models import News, Category
from .utils import MyMixin


def send_feedback(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'tarkovtarkov69@gmail.com', ['suykun228@gmail.com'], fail_silently=True)
            if(mail):
                messages.success(request, 'Письмо успешно отправлено')
                return redirect('feedback')
            else:
                messages.warning(request, 'Ошибка отправки')
        else:
            messages.warning(request, 'Ошибка валидации')
    else:
        form = ContactForm()
    return render(request, 'news/send_feedback.html', {"form": form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
        else:
            messages.warning(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {'form': form})


class HomeNews(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class CategoryNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    paginate_by = 3

    # allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category_title = Category.objects.get(pk=self.kwargs['category_id']).title
        context['title'] = category_title
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class ViewNews(DetailView):
    model = News
    template_name = 'news/view_news.html'
    context_object_name = 'news'
    queryset = News.objects.select_related('category')


class CreateNews(LoginRequiredMixin, CreateView):
    login_url = '/admin/'
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('home')
