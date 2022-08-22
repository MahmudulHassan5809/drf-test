from django.test import SimpleTestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

REQUEST_PAYLOAD = {
    "request_id": "A32W4ER2341",
    "account_name": "TXIuIEFCQw==",
    "amount": "aSN2QHZYeExjRE0h",
}

DECODE_URL = reverse("decode.apis:public:decode")


class DecodeEndpointTestCase(SimpleTestCase):
    def setUp(self):
        self.client = APIClient()

    def test_decode_response(self):
        res = self.client.post(DECODE_URL, REQUEST_PAYLOAD)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["amount"], 1681)
        self.assertEqual(res.data["account_name"], "Mr. ABC")
