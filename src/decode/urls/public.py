from django.urls import path

from decode.views.public import PublicDecodeApiView

app_name = "public"

urlpatterns = [
    path("decode/", PublicDecodeApiView.as_view(), name="decode"),
]
