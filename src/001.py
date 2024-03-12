def display_list(lst):
    print()
    print(*lst, sep='\n', end='\n\n')
    print('-' * 50)


products = [
    {'name': 'Product 5', 'price': 10.00},
    {'name': 'Product 1', 'price': 22.32},
    {'name': 'Product 3', 'price': 10.11},
    {'name': 'Product 2', 'price': 105.87},
    {'name': 'Product 4', 'price': 69.9},
]
display_list(products)

new_products = [
    {**product, 'price': round(product['price'] * 1.1, 2)}
    for product in products
]
display_list(new_products)

products_sorted_by_name = sorted(
    products,
    key=lambda p: p['name'],
    reverse=True,
)
display_list(products_sorted_by_name)

products_sorted_by_price = sorted(
    products,
    key=lambda p: p['price'],
)
display_list(products_sorted_by_price)
