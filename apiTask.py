import requests

url = "https://fakestoreapi.com/products"


response = requests.get(url)

print(response.json()[1])

url="https://fakestoreapi.com/products?sort=desc"
response = requests.get(url)

print(response.json())
print(response.json()[0]['title'])

url="https://fakestoreapi.com/jg"
response = requests.get(url)
print(response.status_code)

new_product = {
    "title": 'test product',
    "price": 13.5,
    "description": 'lorem ipsum set',
    "image": 'https://i.pravatar.cc',
    "category": 'electronic'
}
response = requests.post("https://fakestoreapi.com/products", json=new_product)
print(response.json())