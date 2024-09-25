from django.urls import path
from apps.bookmodule.views import home_view

urlpatterns = [
    path('', home_view, name='home'),  # This route should render home.html
]
