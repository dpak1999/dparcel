from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import views
from core.customer import views as customer_views
from core.courier import views as courier_views

customer_url_patterns = [
    path('', customer_views.home, name="home")
]

courier_url_patterns = [
    path('', courier_views.home, name="home")
]

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # facebook auth url
    path('', include('social_django.urls', namespace='social')),

    # home
    path("", views.home),

    # auth
    path("sign-in/", auth_views.LoginView.as_view(template_name="sign_in.html")),
    path("sign-out/", auth_views.LogoutView.as_view(next_page="/")),
    path("sign-up/", views.sign_up),

    # others
    path("customer/", include((customer_url_patterns, 'customer'))),
    path("courier/", include((courier_url_patterns, 'courier'))),
]
