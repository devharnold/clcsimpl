# simulate card payment
from client.cybersource_client import CyberSourceClient


class ChargeFunc:
    def __init__(self):
        self.client = CyberSourceClient()

    def charge_card(self, amount: str, currency: str, card_details: dict, billing_info: dict):
        # method to charge card on the platform
        payload = {
            "clientReferenceInformation": {
                "code": ""
            },
            "processingInformation": {
                "capture": True
            },
            "paymentInfo": {
                "card": {
                    "number": card_details["number"],
                    "expiration_month": card_details["expiration_month"],
                    "expiration_year": card_details["expiration_year"]
                }
            },
            "OrderInfo": {
                "amountDetails": {
                    "totalAmount": amount,
                    "currency": currency
                },
                "billTo": {
                    "firstName": billing_info["first_name"],
                    "lastName": billing_info["last_name"],
                    "email": billing_info["email"],
                    "phoneNumber": billing_info["phone"],
                    "country": billing_info["country"]
                }
            }
        }

        # send the request to cybresource
        response = self.client.post("/pts/v2/payments", payload)
        return response