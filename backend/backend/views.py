from django.contrib.auth.models import User, Group
import os
from rest_framework import viewsets

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from backend.serializers import UserSerializer, GroupSerializer

print(os.getcwd() + "\\views.py")
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def url_list(request):
    if request.method == "GET":
        urllist = ["a", "b"]
        content = JSONRenderer().render(urllist)
        return Response(content)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

def AlphabeticPageView():
    filenames = {"model": "Group"}
    for root, folder, files in os.walk(os.path.join(os.getcwd())):
        pass
    import json
    list = [1, 2, (3, 4)]  # Note that the 3rd element is a tuple (3, 4)
    return json.dumps(list)