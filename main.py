from bs4 import BeautifulSoup
import pandas as pd
import requests
from util import product_name_price,product_id,product_images,product_info,product_rating,product_details

for page in range(0,1):
    headers = {
    'authority': 'www.amazon.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'fr-FR,fr;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'device-memory': '8',
    'downlink': '10',
    'dpr': '1',
    'ect': '4g',
    'rtt': '100',
    'sec-ch-device-memory': '8',
    'sec-ch-dpr': '1',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-ch-viewport-width': '1600',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',

} 
    link = (f"https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A16225009011%2Cn%3A2811119011&qid=1699375358&ref=sr_pg_{page}")
    r = requests.get(link,headers=headers)
    print(r)
    soup = BeautifulSoup(r.content, 'html.parser')
    product_links = soup.find_all('div',{'class':'sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20'})
    for link in  product_links:
        url = link.find('a',{'class':'a-link-normal s-no-outline'})
        href = url.get('href')
        links = f'https://amazon.com'+href
        req = requests.get(links.split("/ref")[0], headers=headers)
        soupe = BeautifulSoup(req.content, 'html.parser')       
        product_name_prix = product_name_price(soupe)
        product_detail = product_details(soupe)
        product_information = product_info(soupe)
        product_reviews = product_rating(soupe)
        product_picturs = product_images(soupe)
        product_asin = product_id(soupe)
        result = product_name_prix,product_detail,product_information,product_reviews,product_picturs,product_asin
        print(result)



        







