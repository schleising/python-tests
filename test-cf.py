import requests
from rich import print

def update_dns_record(external_ip: str) -> bool:
    url = "https://api.cloudflare.com/client/v4/zones/a11668af409ad2f84d5041671977221f/dns_records/ee9b47c3ea831683c65fea4dbfd214c3"

    payload = {
        "content": external_ip,
        "name": "schleising.net",
        "proxied": False,
        "type": "A",
        "comment": "Domain verification record",
        # "tags": ["owner:dns-team"],
        "ttl": 3600
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer j-HYB1U_x16_VmF0wFod3Yl44sttmfKtEfDU_5Za"
    }

    response = requests.request("PATCH", url, json=payload, headers=headers)

    if response.status_code == 200:
        print('DNS record updated.')
        return True
    else:
        print('Error updating DNS record.')
        return False

def get_external_ip() -> str:
    url = "https://api.ipify.org?format=json"
    response = requests.get(url)
    print(response.json())
    return response.json()['ip']

if __name__ == '__main__':
    external_ip = get_external_ip()
    # update_dns_record(external_ip)
    print('Done.')
