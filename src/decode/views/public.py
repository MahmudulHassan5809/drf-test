import base64

from django.utils.decorators import method_decorator
from decode.views.process import DecodeDataProcess
from rest_framework import status
from rest_framework.generics import views
from rest_framework.response import Response

from base.helpers.constant import ROMAN_TO_DECIMAL_MAPPING
from base.helpers.decorators import exception_handler
from base.helpers.utils import remove_special_chars_from_string
from decode.serializers import DecodeSerializer


class PublicDecodeApiView(views.APIView):
    serializer_class = DecodeSerializer
    swagger_tags = ["Decode Public Api"]

    @method_decorator(exception_handler)
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            account_name, amount = serializer.data.get(
                "account_name"), serializer.data.get("amount")

            process_obj = DecodeDataProcess(account_name, amount)
            decoded_data = process_obj.get_data()

            response_data = {
                "request_id": serializer.data.get("request_id"),
                "account_name": decoded_data.get('account_name'),
                "amount": decoded_data.get('amount'),
            }
            return Response(data=response_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
