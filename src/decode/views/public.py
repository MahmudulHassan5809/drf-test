from django.utils.decorators import method_decorator
from rest_framework.generics import views

from base.helpers.decorators import exception_handler


class AdminExamListCreateApiView(views.APIView):
    swagger_tags = ["Decode Public Api"]

    @method_decorator(exception_handler)
    def post(self, request, *args, **kwargs):
        print("------")
