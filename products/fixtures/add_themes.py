import json

# Load the JSON data from the file
with open('products/fixtures/products.json', 'r') as json_file:
    data = json.load(json_file)

# Function to extract brand from the product name
def add_theme(product):
    category = product['fields']['category']
    if (category == 8 or category == 10):
        product['fields']['has_themes'] = False
    else:
        product['fields']['has_themes'] = True

# Iterate through each product and extract the brand
for product in data:
    add_theme(product)

# Save the updated JSON back to the file
with open('products/fixtures/products.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("Brand information extracted and JSON file updated.")