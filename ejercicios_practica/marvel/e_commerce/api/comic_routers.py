from rest_framework.routers import DefaultRouter

# Tal cual hacíamos con APIView, importamos los
# Viewsets necesarios, ya que no deja de ser una View.
from .viewsets import (
    ListComicViewSet,
    
)

# Con esto indicamos que el router se haga cargo de nuestras
# rutas, por ende, internamente va a generar las rutas automáticamente 
# para cada petición HTTP que hayamos establecido en la view.
router = DefaultRouter()

# Registramos el endpoint y finalmente se lo
# asignamos a "urlpatterns".
# NOTE: Recordar que cuando enlazamos un archivo de rutas, Django
# siempre va intentar buscar en el archivo es que exista la lista
# 'urlpatterns'.
router.register(
    r'modelviewset/filter_comics',
    ListComicViewSet,
    basename='modelviewset/filter_comics'
)

urlpatterns = router.urls