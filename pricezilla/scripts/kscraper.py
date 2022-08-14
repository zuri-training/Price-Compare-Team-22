from selenium import webdriver
from bs4 import BeautifulSoup as BS
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

from product.models import Product, Category, Store

service = Service(executable_path="C:/Users/hp/Desktop/Team 22/local use/pricezilla/scripts/chromedriver.exe")
options = Options()
options.headless = True
options.add_experimental_option('excludeSwitches', ['enable-logging'])

def run():

    def scrape(url, pages, cat):
        for page in range(1, pages):
            browser = webdriver.Chrome(service=service, options=options)
            browser.get(f'{url}{page}')
            delay = 5 # seconds
    
            product = None
            try:
                myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'b49ee_2pjyI')))
                print(f"Page {page} is ready!")
                html_text = browser.page_source
                soup = BS(html_text, 'lxml')
                product = soup.find('ul', class_="b49ee_2pjyI")
            except TimeoutException:
                print(f"Loading page {page} took too much time!")
            browser.close()
            if product is not None:
                product_cards = product.find_all('li')
                for card in product_cards:
                    name = card.h3.text
                    print(name)
                    category = Category.objects.filter(name=cat)
                    store = Store.objects.filter(name='Konga')
                    price = card.find('span', class_='d7c0f_sJAqi').text
                    image = card.source['data-srcset']
                    product_url = 'https://www.konga.com' + card.a['href']
                    if Product.objects.filter(name=name,store=store[0],category=category[0]).exists():
                        
                        product = Product.objects.get(name=name,store=store[0],category=category[0])
                        # Checks the price
                        if product.price != price:
                            product.price = price
                            
                            product.save()
                    else:
                        product = Product(name=name, category=category[0], store=store[0], price=price, image=image, url=product_url)
                        product.save()

    #scrape('https://www.konga.com/category/furniture-6081?page=', 25, 'Furnitures')
    #scrape('https://www.konga.com/category/washers-dryers-1008?page=', 22, 'Laundry')
    #scrape('https://www.konga.com/category/irons-steamers-927?page=', 25, 'Laundry')
    #scrape('https://www.konga.com/category/house-keeping-pet-supplies-2500?page=', 25, 'Laundry')
    #scrape('https://www.konga.com/category/kitchen-dining-2995?page=', 25, 'Kitchen')
    scrape('https://www.konga.com/category/small-appliances-5481?page=', 26, 'Kitchen')
    #scrape('https://www.konga.com/category/televisions-5266?page=', 26, 'Home Entertainment')
    #scrape('https://www.konga.com/category/dvd-players-recorders-5265?page=', 7, 'Home Entertainment')
    #scrape('https://www.konga.com/category/audio-systems-5263?page=', 25, 'Home Entertainment')
    #scrape('https://www.konga.com/category/games-consoles-1683?page=', 25, 'Home Entertainment')
    
    

