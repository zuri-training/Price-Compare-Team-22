import requests
import json
from product.models import Product, Category, Store


def run():
    url = 'https://jiji.ng/api_web/v1/listing?slug=furniture&filter_attr_247_condition=Brand+New&webp=true'
    for page in range(50):
        request = requests.get(url)
        data_dump = json.loads(request.text)
        url = data_dump['next_url']
        products = data_dump['adverts_list']['adverts']

        for product in products:
            name = product['title']
            category = Category.objects.filter(name='Furnitures')
            store = Store.objects.filter(name='Jiji')
            price = product['price_obj']['view']
            image = product['image_obj']['url']
            product_url = product['url']

            if Product.objects.filter(name=name,store=store[0],category=category[0]).exists():
                
                product = Product.objects.get(name=name,store=store[0],category=category[0])
                # Checks the price
                if product.price != price:
                    product.price = price
                    
                    product.save()
            else:
                product = Product(name=name, category=category[0], store=store[0], price=price, image=image, url=product_url)
                product.save()