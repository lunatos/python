import json

with open('vendas.json') as f:
    data = json.load(f)

product_sales = {}
best_selling_product = ''
max_product_value = 0

for order in data['vendas']:
    product = order['produto']
    quantity = order['quantidade']
    price = order['preco']
    total_sales = quantity * price
    
    if total_sales > max_product_value:
        max_product_value = total_sales
        best_selling_product = product

print(f"O produto mais vendido foi o produto: {best_selling_product}") 