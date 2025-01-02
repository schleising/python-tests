import requests


BASE_URL = "http://192.168.1.1:8000/webapi"
LOGIN_URL = f"{BASE_URL}/auth.cgi"


def main() -> None:
    params = {
        "api": "SYNO.API.Auth",
        "method": "login",
        "version": "3",
        "account": "username",
        "passwd": "password",
    }

    response = requests.get(
        url=LOGIN_URL,
        verify=False,
        params=params,
    )

    print(f"Status code: {response.status_code}")
    print(response.json())

    cookies = {
        "id": response.json()["data"]["sid"],
    }

    params["api"] = "SYNO.Core.DDNS.ExtIP"
    # params["api"] = "SYNO.API.Info"
    # params["api"] = "SYNO.Core.Network.Ethernet"
    params["method"] = "list"
    params["version"] = "1"
    del params["account"]
    del params["passwd"]

    response = requests.get(
        url=f"{BASE_URL}/entry.cgi",
        verify=False,
        params=params,
        cookies=cookies,
    )

    print("Getting DDNS IP address")
    print(f"Status code: {response.status_code}")
    print(response.json())

    print()
    print(f"IP address: {response.json()['data'][0]['ip']}")

    params["api"] = "SYNO.API.Auth"
    params["method"] = "logout"
    params["version"] = "3"

    print()
    print("Logging out")

    response = requests.get(
        url=LOGIN_URL,
        verify=False,
        params=params,
        cookies=cookies,
    )

    print(f"Status code: {response.status_code}")
    print(response.json())

    print()
    print("Logged out")
    print()

    print("Trying to get DDNS IP address again")

    params["api"] = "SYNO.Core.DDNS.ExtIP"
    params["method"] = "list"
    params["version"] = "1"

    response = requests.get(
        url=f"{BASE_URL}/entry.cgi",
        verify=False,
        params=params,
        cookies=cookies,
    )

    print("Getting DDNS IP address")
    print(f"Status code: {response.status_code}")
    print(response.json())

    print()
    print(f"IP address: {response.json()['data'][0]['ip']}")


if __name__ == "__main__":
    main()
