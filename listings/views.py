from django.shortcuts import render, get_object_or_404
from .models import Post,Category
from django.contrib.auth.models import User
from inquiry.models import Contact
from core.models import Team
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from taggit.models import Tag
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .modelchoices import location_choices
from .forms import EmailPostForm
from django.db.models import Q

# Create your views here.

def search(request):
    query = request.GET.get('query', '')
    listings = Post.published.filter(Q(address__icontains=query) | Q(body__icontains=query))

    return render(request, 'listings/search.html', {'listings': listings, 'query': query})

class PostDashboardView(LoginRequiredMixin, ListView):
    model = Contact
    context_object_name = 'post_list_dashboard'
    query = Contact.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PostDashboardView, self).get_context_data(**kwargs)
        context['choice_list'] = location_choices
        return context

    template_name = 'listings/post_dashboard.html'

    def get_queryset(self):
        return Contact.objects.filter(user_id=self.request.user.id)
    
def blog_category(request, category_slug):
    teams = Team.objects.all()
    categories = Category.objects.all()
    posts = Post.published.filter(status='published')
    if category_slug:
        category = get_object_or_404(Category, slug= category_slug)
        posts = Post.published.filter(category=category)
   
    context = {
        "categories": categories,
        "posts": posts,
        "category": category,
        "teams": teams,
    }
    
    return render(request, "listings/categories.html", context)

def listings(request, tag_slug=None):
    teams = Team.objects.all()
    posts = Post.published.all()
    tag = None
    
    if tag_slug:
        tag = get_object_or_404(Tag,slug=tag_slug)
        posts = posts.filter(tags__in=[tag])
        
    paginator = Paginator(posts,3)# 3 posts at single page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    template = 'listings/listings.html'
    
    context = {
        'page': page,
        'posts': posts,
        'teams': teams,
        'tag': tag,
    }
    
    return render(request, template, context)



def listing(request,listing_id):
    teams = Team.objects.all()
    post = get_object_or_404(Post, pk=listing_id, status='published')

    template = 'listings/listing.html'

    data = {
        'post': post,
        'teams' : teams,
        #'comments': comments,
        #'comment_form': comment_form,
        #'post_tags_ids': post_tags_ids,
        #'similar_posts': similar_posts,
    }

    return render(request, template, data)

def post_share(request, post_id):
    teams = Team.objects.all()
    post =  get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #  ... send data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read" f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n" f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject,message,'sewemallonline@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    
    template = 'listings/share.html'
    
    context = {
        'post' : post,
        'form' : form,
        'sent' : sent,
        'teams': teams,
    }
    
    return render(request, template, context)

