import json
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from.models import *


@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    category_json = categories.serializer.serializ('json',categories)
    return Response({'data': category_json})


@api_view(['POST'])
def create_categories(request):
    name = ""
    description = ""
    model_category = Category.create(name=name, description=description)
    model_category.save()
    return Response({'data': model_category})
