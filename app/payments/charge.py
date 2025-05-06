# simulate card payment
import requests
import json
from app.client.cybersource_client import CyberSourceClient


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
                "amountDetails": 
            }
        }