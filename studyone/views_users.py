from django.http import JsonResponse
from studyone.form_user import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import  status
from studyone.models import users
import json
import pymysql

@api_view(['GET'])
def userlist(request):
    if request.method == 'GET':
        queryset = request.GET.get('id')
        user_list = users.objects.order_by('-id')

        if queryset:
            user_list = users.objects.filter(id=queryset)
        else:
            user_list = users.objects.all()

        serializer = UserSerializer(user_list, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def adduser(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        body = {
            'body':serializer.errors,
            'msg':'400001'
        }
        return Response(body, status=status.HTTP_200_OK)




@api_view(['POST'])
def deleteuser(request):
    # print(request.POST)
    print(request.body)
    try:
        # id = json.loads(request.body).get('id')
        deleteuser = users.objects.filter(id=id)
        deleteuser.delete()
        return Response("删除用户成功",status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response("用户不存在,无法删除!", status=status.HTTP_200_OK)












