from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('students/', views.students, name='students'),
    path('students_data/', views.students_json),
    path('submit', views.submit, name='submit'),
    path('products/', views.products, name='products'),
    path('categories/', views.categories, name='categories'),
    path('products/<int:id>', views.get_product),
    path('review', csrf_exempt(views.add_review)),
    path('items/', views.items),
    path('items/<int:id>', views.get_item),
    path('ratings', views.ratings),
    path('contact', views.contact),
    path('contact_form', views.contact_form),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)