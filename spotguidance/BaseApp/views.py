from rest_framework.decorators import api_view, APIView
from rest_framework.decorators import APIView
from .models import Category, SubCategory, Spot
from .serializers import CategorySerializers, SubcategorySerializers, SpotSerializers
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def api_overview(request):
    apis = {
        'category-list': '/Categories',
        'subcategory-list': '/Subcategories',
        'spot-list': '/Spots',
    }
    return Response(apis)

class Category_list(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializers(categories, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CategorySerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def update(self, request, pk, format=None):
        try:
            category = get_object_or_404(Category, id=pk)
            serializer = CategorySerializers(category, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except:
            return Response({'Error': 'Category Not Found'})

    def delete(self, request, pk, format=None):
        try:
            category = get_object_or_404(Category, id=pk)
            category.delete()
            return Response({'Message': 'Category deleted successfully !'})
        except:
            return Response({'Error': f'Category with ID {pk} was Not Found'})

class Subcategory_list(APIView):
    def get(self, request, format=None):
        sub_category = SubCategory.objects.all()
        serializers = SubcategorySerializers(sub_category, many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializer = SubcategorySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def update(self, request, pk, format=None):
        try:
            subcategory = get_object_or_404(SubCategory, id=pk)
            serializer = CategorySerializers(subcategory, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except:
            return Response({'Error': 'subcategory Not Found'})
        
    def delete(self, request, pk, format=None):
        try:
            subcategory = get_object_or_404(SubCategory, id=pk)
            subcategory.delete()
            return Response({'Message': 'SubCategory deleted successfully !'})
        except:
            return Response({'Error': f'SubCategory with Id {pk} was Not Found'})

class Spot_list(APIView):
    def get(self, request, format=None):
        spots = Spot.objects.all()
        serializers = SpotSerializers(spots, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        data = request.data
        serializer = SpotSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class Spot_detail(APIView):
    def get_object(self, pk):
        try:
            spot = get_object_or_404(Spot, id=pk)
            return spot
        except:
            return None
        
    def get(self, request, pk, format=None):
        spot = self.get_object(pk=pk)
        if spot:
            return Response(SpotSerializers(spot).data)
        else:
            return Response({'Error': 'Spot not found !'})

    def put(self, request, pk, format=None):
        spot = self.get_object(pk=pk)
        if spot:
            serializer = SpotSerializers(spot, data = request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response({'Error': 'Spot Not Found'})
        
    
    def delete(self, request, pk, format=None):
        spot = self.get_object(pk=pk)
        if spot:
            spot.delete()
            return Response({'Message': 'Spot deleted successfully !'})
        else:
            return Response({'Error': f'Spot with Id {pk} was Not Found'})