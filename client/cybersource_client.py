import hashlib
import hmac
import base64
import uuid
import httpx
from datetime import datetime
from urllib.parse import urlparse
from app.config import settings


class CyberSourceClient:
    def __init__(self):
        self.api_key = settings.CYBERSOURCE_API_KEY
        self.secret = settings.CYBERSOURCE_SECRET
        self.base_url = settings.CYBERSOURCE_BASE_URL
        self.merchant_id = settings.CYBERSOURCE_MERCHANT_ID

    async def charge_card(self, payload: dict):
        path = "/pts/v2/payments"
        url = self.base_url + path
        method = "POST"
        body = httpx.dumps(payload, separators=(",", ":")) if isinstance(payload, dict) else payload

        digest = self.create_digest(body)
        date = self.get_http_date()
        headers = {
            "host": urlparse(self.url).netloc,
            "date": date,
            "digest": digest,
            "v-c-mechanic-id": self.merchant_id
        }

        signature = self.generate_signature(method, path, headers)
        headers["signature"] = signature
        headers["content-type"] = "application/json"

        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=payload)
            return response.json()
        
    def create_digest(self, body: str) -> str:
        # returns a string
        digest = hashlib.sha256(body.encode("utf-8")).digest()
        return f"SHA-256={base64.b64encode(digest).decode()}"
    
    def get_http_date(self) -> str:
        return datetime.now().strftime("%a, %d, %b, %Y, %H:%M:%S GMT")
    
    def generate_signature(self, method, path, headers) -> str:
        signature_header = [
            f"(request-target): {method.lower()} {path}",
            f"host: {headers["host"]}",
            f"date: {headers["date"]}",
            f"digest: {headers["digest"]}",
            f"v-c-merchant_id: {headers["v-c-merchant_id"]}",
        ]
        signature_string = "\\n".join(signature_header)
        signature_byte = hmac.new(
            base64.b64decode(self.share_secret),
            msg = signature_string.encode("utf-8"),
            digestmod=hashlib.sha256
        ).digest()

        signature_encoded = base64.b64encode(signature_byte).decode()

        return (
            f'key_id="{self.api_key}", algorithm=HmacSHA256", '
            f'headers="(request-target) host date digest v-c-merchant_id", '
            f'signature="{signature_encoded}" '
        )
    
