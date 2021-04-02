from rest_framework.viewsets import ModelViewSet

from products.models import Product
from products.serializers import ProductSerializer


class ProductsView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()