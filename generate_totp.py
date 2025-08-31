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