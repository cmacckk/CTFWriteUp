# coding=utf-8
import hmac
import hashlib
import base64

key = '1Kun'

header = '{"alg": "HS256","typ": "JWT"}'
payload = '{"username": "admin"}'

encodeHBytes = base64.urlsafe_b64encode(header.encode("utf-8"))
encodeHeader = str(encodeHBytes, "utf-8").rstrip("=")

encodePBytes = base64.urlsafe_b64encode(payload.encode("utf-8"))
encodePayload = str(encodePBytes, "utf-8").rstrip("=")

token = (encodeHeader + "." + encodePayload)


sig = base64.urlsafe_b64encode(hmac.new(bytes(key, "UTF-8"), token.encode("utf-8"), hashlib.sha256).digest()).decode("UTF-8").rstrip("=")

print(token + "." + sig)