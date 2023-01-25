from rest_framework import viewsets,views
from .models import Product,Variant
from Inventory.serializer import ProductSerializer,VariantSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True,methods=['get'])
    def variants(self,request,pk=None):   
        try:
                      
            product=Product.objects.get(uid=pk)
            print(product)     
            variants=Variant.objects.filter(product=product)
            variants_serializer=VariantSerializer(variants,many=True,context={'request':request})
            return Response(variants_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Product might not exists !! Error'
            })

class ProductListApiView(views.APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class VariantViewSet(viewsets.ModelViewSet):
    queryset=Variant.objects.all()
    serializer_class=VariantSerializer