import json

with open('products/fixtures/products.json', 'r') as json_file:
    data = json.load(json_file)

i = 1
for product in data:
    if product['pk'] >= 148 and product['pk'] <= 155:

        product['fields']['image'] = f'gauntlets-{i}.png'
        product['fields']['image_url'] = f'https://ci-pp5-infinity-innovations.s3.eu-west-1.amazonaws.com/media/item+category+data/Digital+World/Armour/gauntlets/gauntlets-{i}.png'
        i += 1

with open('products/fixtures/products.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("JSON file updated successfully.")