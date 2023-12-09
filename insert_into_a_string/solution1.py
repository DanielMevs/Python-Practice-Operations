def add_product_code(product_code, product_id):
    # Your code goes here
    if product_id[4:9] == product_code:
        return product_id
    else:
        first_part = product_id[:3]
        last_part = product_id[3:]
        return f'{first_part}-{product_code}-{last_part}'