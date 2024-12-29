from rest_framework.routers import DefaultRouter
from django.urls import path
from products.views import ProductViewSet, CategoryViewSet, UserViewSet, OrderViewSet, ProductListView, OrderItemView, ProductReviewSet
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter() # create default router

router.register('view-products', ProductListView, basename='view-products') # register view for products
router.register('products', ProductViewSet) # register view for products
router.register('users', UserViewSet) # register view for users
router.register('orders', OrderViewSet) # register view for orders
router.register('category', CategoryViewSet) # register view for categories
router.register('order-item', OrderItemView) # register view for order items
router.register('reviews', ProductReviewSet) # register view for product reviews
#router.register('search', ProductFilter, basename='product_filter')

urlpatterns = [path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),] + router.urls # add token url to urlpatterns
