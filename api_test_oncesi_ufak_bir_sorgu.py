import requests


def usom_requests():
    URL = "https://www.usom.gov.tr/api/address-description/index"

    response = requests.get(
        URL,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel)",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
            "Accept": "application/json, text/plain, */*",
            "Origin": "https://www.usom.gov.tr",
            "DNT": "1",
            "Sec-Fetch-Dest": "empty",
            "Connection": "keep-alive",
            "Host": "www.usom.gov.tr",
            "Referer": "https://www.usom.gov.tr/",
        },
        params={"page": 1},
    )

    data = response.json()
    if "models" in data:
        return data
    else:
        print("No models found")


def usomAppService(data) -> str:
    for item in data["models"]:
        print("ID:", item["id"])
        print("TR Title:", item["tr_title"])
        print("EN Title:", item["en_title"])
        print("TR Description:", item["tr_desc"])
        print("EN Description:", item["en_desc"])


response = usom_requests()
if response:
    usomAppService(response)
