import json

import requests
from requests.status_codes import codes

response = requests.get("http://localhost:8000/items/2?q=name")

if response.status_code == codes.ok:
    print(json.dumps(json.loads(response.content), indent=2))
