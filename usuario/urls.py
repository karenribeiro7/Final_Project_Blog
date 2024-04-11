from django.urls import path
from .views import logout_user

urlpatterns = [
    # Outras URLs da sua aplicação...
    path('logout/', logout_user, name='logout'),
]