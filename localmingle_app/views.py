from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from localmingle_app.models import Contact, Blog, Newsletter
from localmingle_app.serializers import ContactSerializer, NewsletterSerializer


@permission_classes((AllowAny, ))
@method_decorator(csrf_exempt, name='dispatch')
class ContactViewSet(viewsets.ModelViewSet):
    
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


@permission_classes((AllowAny, ))
@method_decorator(csrf_exempt, name='dispatch')
class NewsletterViewSet(viewsets.ModelViewSet):
    
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer


class HomePageView(ListView):

    template_name = 'index.html'
    queryset = Blog.objects.all().order_by('-created_on')[:3]
    context_object_name = 'blogs'


class BlogListing(ListView):

    template_name = 'blog.html'
    queryset = Blog.objects.all().order_by('-created_on')
    context_object_name = 'blogs'

class BlogDetail(DetailView):

    model = Blog
    template_name = 'blog-detail.html'