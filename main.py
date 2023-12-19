import requests
import json


def get_category():
    url = 'https://catalog.wb.ru/catalog/head_accessories3/catalog?TestGroup=no_test&TestID=no_test&appType=1&cat=9967&curr=rub&dest=-1257786&sort=popular&spp=27'

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Origin': 'https://www.wildberries.by',
        'Referer': 'https://www.wildberries.by/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'sec-ch-ua': 'Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'macOS',
    }

    # response = requests.get(url=url, headers=headers, proxies=proxies)
    response = requests.get(url=url, headers=headers)
    return response.json()

def prepare_items(response):
    products = []

    products_raw = response.get('data', {}).get('products', None)

    if products_raw != None and len(products_raw) > 0:
        for product in products_raw:
            products.append({
                'brand': product.get('brand', None),
                'name': product.get('name', None),
                'sale': product.get('sale', None),
                'priceU': float(product.get('priceU', None)) / 100 if product.get('priceU', None) != None else None,
                'salePriceU': float(product.get('salePriceU', None)) / 100 if product.get('salePriceU',
                                                                                          None) != None else None,
            })
            

    return products

def InFileJson(products):
    for item in range(0, len(products)):
        with open(f'{item } catalog.wb.ru.json', 'w', encoding='utf8') as json_file:
            json.dump(products[item], json_file, ensure_ascii=False, indent=4)

def main():
    response = get_category()
    products = prepare_items(response)
    InFileJson(products)


if __name__ == '__main__':
    main()