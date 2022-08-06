from bs4 import BeautifulSoup as bs
import requests
from product.models import Product, Category, Store

def run():
    for page in range(50):
        head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive'}

        html_text = requests.get(f'https://www.jumia.com.ng/home-living-room-furniture/?shipped_from=country_local&page={page}', head).text
        soup = bs(html_text, 'lxml')

        product_cards = soup.find_all('article', class_="prd _fb col c-prd")
        for card in product_cards:
            name = card.find('h3', class_='name').text
            category = Category.objects.filter(name='Furnitures')
            store = Store.objects.filter(name='Jumia')
            price = card.find('div', class_='prc').text
            image = card.find('img', class_='img')['data-src']
            url = 'https://www.jumia.com.ng' + card.a['href']
            print(name)
            if Product.objects.filter(name=name,store=store[0],category=category[0]).exists():
                
                product = Product.objects.get(name=name,store=store[0],category=category[0])
                # Checks the price
                if product.price != price:
                    product.price = price
                    
                    product.save()
            else:
                product = Product(name=name, category=category[0], store=store[0], price=price, image=image, url=url)
                product.save()