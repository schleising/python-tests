import json

import requests

with open("hue_monitor.json", "r") as f:
    data = json.load(f)

response = requests.get(
    url="https://192.168.1.83/clip/v2/resource/temperature/3ff550e4-d792-491f-920b-f5269b5ea93d",
    headers={
        "hue-application-key": data["username"],
        "Content-Type": "application/json",
    },
    verify=False,
)

print(response)
response_json = json.dumps(json.loads(response.text), indent=2)
print(response_json)

with open("hue_temperature_list.json", "w") as f:
    f.write(response_json)
