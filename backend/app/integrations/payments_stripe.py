import hmac
import json
from hashlib import sha256


def create_checkout_session_stub(order_id: str) -> dict:
    return {"id": f"cs_test_{order_id}", "url": f"https://checkout.stripe.test/{order_id}"}


def verify_signature(payload: bytes, signature: str, secret: str) -> bool:
    expected = hmac.new(secret.encode(), payload, sha256).hexdigest()
    return hmac.compare_digest(signature, expected)


def parse_event(payload: bytes) -> dict:
    return json.loads(payload.decode("utf-8"))
