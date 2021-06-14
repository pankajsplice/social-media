from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers

from localmingle_app.views import ContactViewSet, BlogListing, BlogDetail, NewsletterViewSet, HomePageView

router = routers.DefaultRouter()
router.register(r'contact', ContactViewSet)
router.register(r'newsletter', NewsletterViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', HomePageView.as_view(), name='index'),
    path('blog/', BlogListing.as_view(), name='blog'),
    path('contact', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('privacy', TemplateView.as_view(template_name='privacy.html'), name='privacy'),
    path('termof', TemplateView.as_view(template_name='termof.html'), name='termof'),
    path('<slug:slug>/', BlogDetail.as_view(), name='blog-detail'),
]
