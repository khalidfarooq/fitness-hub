from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

from .serializers import userInfoSerializer

from .models import userInfo


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'userInfo': 'user-info',
    }

    return Response(api_urls)


@api_view(['GET'])
def userInfo(request):
    userDetails = userInfo.objects.all().order_by('-id')
    serializer = userInfoSerializer(userDetails, many=True)
    return Response(serializer.data)
