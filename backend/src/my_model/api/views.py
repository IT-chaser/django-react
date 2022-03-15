from rest_framework.generics import ListAPIView

from .serializers import MyProductSerializer
from my_model.models import MyProduct
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def add_product(request):
    ip = get_client_ip(request)
    serializer = MyProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(requester_ip=ip)
    return Response(serializer.data)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip