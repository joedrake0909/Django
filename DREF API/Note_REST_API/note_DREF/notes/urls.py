from rest_framework.routers import DefaultRouter
from .views import NoteViewSet

router = DefaultRouter()

router.register(
    prefix='notes',
    viewset=NoteViewSet,
    basename='note',
)

urlpatterns = router.urls

