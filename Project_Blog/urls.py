from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from cadastro.views import cadastroModelViewSet
from django.conf import settings
from django.conf.urls.static import static
from cadastro.views import cadastrar, login, paineldousuario, gerenciar_perfil
from inicio.views import inicio, sobre, contato
from post.views import Post

router = SimpleRouter(trailing_slash=False)
router.register('cadastro', cadastroModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio , name='inicio'), #ok
    path('cadastro/', cadastrar, name='cadastrar'), # ok
    path('login/', login , name='login'), #OK
    #path('usuario/', usuario),  #OK   
    path('sobre/', sobre, name='sobre'), #OK
    path('contato/', contato, name='contato'), #OK
    path('post/', Post, name='post'), #OK
    path('paineldousuario/', paineldousuario, name='paineldousuario'), #OK
    path('gerenciar_perfil/', gerenciar_perfil, name='gerenciar_perfil'), #OK
]
urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
