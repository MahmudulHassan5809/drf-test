from django.urls import include, path

app_name = "decode"

urlpatterns = [
    path("public/", include("decode.urls.public"), name="public.api"),
]
