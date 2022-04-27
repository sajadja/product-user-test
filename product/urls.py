from django.urls import path

from product.views import ProductCreateAPIView

urlpatterns = [
    path('add', ProductCreateAPIView.as_view(), name='add-product')
]
