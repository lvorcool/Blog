from rest_framework import status
from rest_framework.decorators import api_view
from studyone.form_transfermoney import TransferMoneySerializer
from rest_framework.response import Response

@api_view(['POST'])
def transfermoney(request):
    if request.method == 'POST':
        transfermoney = TransferMoneySerializer(data=request.data)
        if transfermoney.is_valid():
            transfermoney.save()
            return Response(transfermoney.data, status=status.HTTP_201_CREATED)

        body = {
            'body':transfermoney.errors,
            "msg":"4000001"
        }
        return Response(body, status=status.HTTP_200_OK)

