import requests
import base64
import time
import hmac
import hashlib

def generate_totp(email):
    secret = (email + "HENNGECHALLENGE004").encode('utf-8')
    tc = int(time.time()) // 30
    msg = tc.to_bytes(8, 'big')
    h = hmac.new(secret, msg, hashlib.sha512).digest()
    offset = h[-1] & 0x0f
    bin_code = ((h[offset] & 0x7f) << 24) | ((h[offset + 1] & 0xff) << 16) | ((h[offset + 2] & 0xff) << 8) | (h[offset + 3] & 0xff)
    return f"{bin_code % 10000000000:010d}"

email = "kuldeepnkunsh@gmail.com"
totp = generate_totp(email)
print(f"Generated TOTP: {totp}")
auth_str = f"{email}:{totp}"
base64_auth = base64.b64encode(auth_str.encode('utf-8')).decode('utf-8')
print(f"Base64 Auth: {base64_auth}")

with open('mission3.json', 'r') as file:
    json_data = file.read()

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Basic {base64_auth}"
}

print(f"Headers: {headers}")
print(f"JSON Data: {json_data}")

response = requests.post("https://api.challenge.hennge.com/challenges/backend-recursion/004", data=json_data.encode('utf-8'), headers=headers)
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")