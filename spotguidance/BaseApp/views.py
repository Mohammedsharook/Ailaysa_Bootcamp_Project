from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, APIView
from .models import Category, SubCategory
from .serializers import CategorySerializers, SubcategorySerializers


@api_view(['GET'])
def api_overviews(request):
    apis = {
        'category-list': '/Categories',
        'subcategory-list': '/Subcategories',
        'spot-list': '/Spots',
    }
    return Response(apis)

@api_view(['GET'])
def category_list(request):
    category = Category.objects.all()
    serializers = CategorySerializers(category, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def subcategory_list(request):
    sub_category = SubCategory.objects.all()
    serializers = SubcategorySerializers(sub_category, many=True)
    return Response(serializers.data)
