from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)

from .models import Post, Vacancies, Applications, HrDocs
from .forms import ApplicationForm



#home page in class list view
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


#display user posts in class list view
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html' #<app>/<model>_<viewtype>.html

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class VacanciesListView(ListView):
    model = Vacancies
    paginate_by = 5

    def get_queryset(self):
        return Vacancies.objects.filter().order_by('-date_posted')


class VacanciesDetailView(DetailView):
    model = Vacancies
    template_name = 'blog/vacancies_detail.html' #<app>/<model>_<viewtype>.html    

#create job aplication
def create_application(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.date_applied = timezone.now()
            post.save()
            messages.success(request, f'Your application has been received, kindly note only short listed candidates will be contacted. ')
            return redirect('vacancies-home')
    else:
        form = ApplicationForm()
    return render(request, 'blog/application_form.html', {'form': form})

#home page in class list view
class HrdocListView(ListView):
    model = HrDocs
    template_name = 'blog/Hr_doc.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_uploaded']
    paginate_by = 5
    

