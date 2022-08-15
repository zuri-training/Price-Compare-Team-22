from bs4 import BeautifulSoup as bs
import requests
from product.models import Product, Category, Store
import codecs

def run():

    def scrape(url, pages, cat):
        for page in range(1, pages):
            try:
                head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                        'Accept-Encoding': 'none',
                        'Accept-Language': 'en-US,en;q=0.8',
                        'Connection': 'keep-alive'}
                res = requests.get(f'{url}{page}', head)
                html_text = res.text
                res.close()
                soup = bs(html_text, 'lxml')

                product_cards = soup.find_all('article', class_="prd _fb col c-prd")
                for card in product_cards:
                    name = card.find('h3', class_='name').text
                    print(name)
                    category = Category.objects.filter(name=cat)
                    store = Store.objects.filter(name='Jumia')
                    price = card.find('div', class_='prc').text
                    image = card.find('img', class_='img')['data-src']
                    product_url = 'https://www.jumia.com.ng' + card.a['href']
                    res = requests.get(product_url, head)
                    html_text = res.text
                    res.close()
                    soup = bs(html_text, 'lxml')
                    description = soup.find('meta', property="og:description")
                    description = codecs.escape_decode(bytes(description['content'], "utf-8"))[0].decode("utf-8")
                    if not description:
                        continue
                    if Product.objects.filter(name=name,store=store[0],category=category[0]).exists():
                        
                        product = Product.objects.get(name=name,store=store[0],category=category[0])
                        # Checks the price
                        if product.price != price:
                            product.price = price
                        if product.description != description:
                            product.description = description
                            
                            product.save()
                    else:
                        product = Product(name=name, description=description, category=category[0], store=store[0], price=price, image=image, url=product_url)
                        product.save()
            except:
                continue

    #scrape('https://www.jumia.com.ng/home-kitchen-furniture/?shipped_from=country_local&page=', 50, 'Furnitures')
    scrape('https://www.jumia.com.ng/ironing-laundry/?shipped_from=country_local&page=', 30, 'Laundry')
    scrape('https://www.jumia.com.ng/home-kitchen-dining/?shipped_from=country_local&page=', 50, 'Kitchen')
    scrape('https://www.jumia.com.ng/home-audio-electronics/?shipped_from=country_local&page=', 50, 'Home Entertainment')
    scrape('https://www.jumia.com.ng/electronic-television-video/?shipped_from=country_local&page=', 50, 'Home Entertainment')
