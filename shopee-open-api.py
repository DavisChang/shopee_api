import hmac
import time
import hashlib

timestamp = int(time.time())
print('timestamp:', timestamp)
# host = 'https://partner.shopeemobile.com'
host = "https://partner.test-stable.shopeemobile.com"
path = "/api/v2/shop/auth_partner"
redirect_url = 'https://google.com/'
partner_id = 'partner_id'
partner_key = 'partner_key'
base_string = f'{partner_id}{path}{timestamp}'
print('base_string: ', base_string)


partner_key = partner_key.encode()
base_string = base_string.encode()

sign = hmac.new(partner_key, base_string, hashlib.sha256).hexdigest()
print('sign: ', sign)

url = host + path + "?partner_id=%s&timestamp=%s&sign=%s&redirect=%s"%(partner_id, timestamp, sign, redirect_url)
print('Authorization url: ', url)

# get code from url
# https://images.google.com/?code=code&shop_id=shop_id
code = "6f47747676437676707844427364596b"

prod_host = 'https://partner.shopeemobile.com'
test_host = 'https://partner.test-stable.shopeemobile.com'
shop_id = 'shop_id'
print('prod_host: ', prod_host)
print('test_host: ', test_host)
print('shop_id: ', shop_id)