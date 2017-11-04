from django.http import JsonResponse
from studyone.form_user import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import  status
from studyone.models import users

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

def deleteuser(request, usersname):

    if request.method == 'POST':
        queryset = users.objects.filter(usersname)
        if queryset:
            deleteuser = users.objects.filter(usersname=usersname)
            deleteuser.detele()
            return Response(status=status.HTTP_200_OK)
        else:
            body = {
                    'msg': '该用户不存在'
                }
            return Response(body, status=status.HTTP_200_OK)





'''
        queryset = request.GET.get('id')
        user_list = users.objects.order_by('-id')

        if queryset:
            user_list = users.objects.filter(id=queryset)
        else:
            user_list = users.objects.all()
'''


'''
@api_view(['POST'])
def adduser(request):

    if request.method == "POST":
        form = UserForm(data=request.data)
        if form.is_valid():
            usersname = UserForm["usersname"]
            password = UserForm["password"]
            name = UserForm["name"]
            u = UserForm(usersname=usersname, password=password,name=name)
            u.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            print("你确定错了吗")
            body = {
                'body':serializers.errors,
                'msg':'400001'
            }
            return JsonResponse(body, status=status.HTTP_400_BAD_REQUEST)
'''


#
# result = users.objects.filter(id=id)
# if result:
#     return JsonResponse({'status':10022, 'message':'用户id已存在,请重新填写'})
#
# result = users.objects.filter(usersname=usersname)
# if result:
#     return JsonResponse({'status':10023, 'message': '用户账号已存在,请重新填写'})



