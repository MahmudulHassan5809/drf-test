import base64

from django.utils.decorators import method_decorator
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
            account_name = base64.b64decode(serializer.data.get("account_name")).decode(
                "utf-8"
            )
            amount_decode_value = remove_special_chars_from_string(
                base64.b64decode(serializer.data.get("amount")).decode("utf-8")
            ).upper()

            amount = sum(
                [ROMAN_TO_DECIMAL_MAPPING.get(char, 0) for char in amount_decode_value]
            )
            response_data = {
                "request_id": serializer.data.get("request_id"),
                "account_name": account_name,
                "amount": amount,
            }
            return Response(data=response_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
