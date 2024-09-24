from rest_framework.decorators import APIView
from .models import Category, SubCategory, Spot
from .serializers import CategorySerializers, SubcategorySerializers, SpotSerializers
from rest_framework.response import Response

class Category_list(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializers(categories, many=True)
        return Response(serializer.data)

class Subcategory_list(APIView):
    def get(self, request, format=None):
        sub_category = SubCategory.objects.all()
        serializers = SubcategorySerializers(sub_category, many=True)
        return Response(serializers.data)
    
class Spot_details(APIView):
    def get(self, request, format=None):
        spots = Spot.objects.all()
        serializers = SpotSerializers(spots, many=True)
        return Response(serializers.data)
