from django.urls import path, include
from Inventory.views import ProductViewSet, ProductListApiView, VariantViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'variants', VariantViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('list/', ProductListApiView.as_view(), name='product-list'),
]
