from rest_framework.routers import DefaultRouter

from app.pkg.two_sum.api import views

router = DefaultRouter(trailing_slash=False)
router.register(
    r'two-sum', views.TwoSumView, basename='two_sum'
)

urlpatterns = router.urls
