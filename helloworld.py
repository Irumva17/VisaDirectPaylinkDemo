import requests
import json
from data import user_id, password, cert, key

url = 'https://sandbox.api.visa.com/vdp/helloworld'

timeout = 30

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

payload = json.loads("""{}""")

response = requests.get(
    url,
    # verify=False,
    cert=(cert, key),
    auth=(user_id, password),
    headers=headers,
    json=payload,
    timeout=timeout
)

print("Status Code:", response.status_code)
print("Response Body:", response.text)