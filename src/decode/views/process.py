import base64
from dataclasses import dataclass
from base.helpers.constant import ROMAN_TO_DECIMAL_MAPPING

from base.helpers.utils import remove_special_chars_from_string


@dataclass
class DecodeDataProcess:
    account_name: str
    amount: str

    def decode_account_name(self):
        return base64.b64decode(self.account_name).decode("utf-8")

    def decode_amount(self):
        amount_decode_value = remove_special_chars_from_string(
            base64.b64decode(self.amount).decode("utf-8")).upper()

        return sum(
            [ROMAN_TO_DECIMAL_MAPPING.get(char, 0)
             for char in amount_decode_value]
        )

    def get_data(self):
        return {
            "account_name": self.decode_account_name(),
            "amount": self.decode_amount(),
        }
