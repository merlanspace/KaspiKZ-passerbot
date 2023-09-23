import requests
import json

url = 'https://kaspi.kz/yml/offer-view/offers/106363303'

headers = {
    "Host": "kaspi.kz",
    "Connection": "keep-alive",
    "Content-Length": "318",
    "sec-ch-ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
    "CSRFToken": "undefined",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Content-Type": "application/json; charset=UTF-8",
    "Accept": "application/json, text/*",
    "X-KS-City": "750000000",
    "sec-ch-ua-platform": "\"Windows\"",
    "Origin": "https://kaspi.kz",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://kaspi.kz/shop/p/apple-iphone-14-pro-max-128gb-fioletovyi-106363303/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-KZ,ru;q=0.9",
    "Cookie": "k_stat=3404648b-afb1-4fd7-9174-1c663b9d89d0; ks.tg=91"
}

# Данные JSON для запроса
data = {
    "cityId": "750000000",
    "id": "106363303",
    "merchantUID": "",
    "limit": 5,
    "page": 0,
    "sort": True,
    "product": {
        "brand": "Apple",
        "categoryCodes": ["Smartphones", "Smartphones and gadgets", "Categories"],
        "baseProductCodes": ["[Master - Smartphones][apple]{iPhone 14 Pro Max}"],
        "groups": None
    },
    "zoneId": "Magnum_ZONE1",
    "installationId": "-1"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    json_data = response.json()

    offers = json_data.get('offers', [])
    for offer in offers:
        merchant_name = offer.get('merchantName', 'Unknown')
        price = offer.get('price', 'N/A')
        print(f"Магазин: {merchant_name}, Цена: {price}")
else:
    print(f"Ошибка {response.status_code}: {response.text}")
