#Global varibles needed for function

product_table=[]

#Function to test

def third_nf(data):
    order_table = []
    order_products = []
    product_id = 0
    try:
        # loop through the data
        for entry in data:
            order_id = entry['id']
            #  Create dictionary for orders
            #  Check if order already exists in order_table
            order_exists = False
            for order in order_table:
                if order['order_id'] == order_id:
                    order_exists = True
                    break
            if not order_exists:
                order_table.append({
                    'order_id': order_id,
                    'date_time': entry['date_time'],
                    'branch_location': entry['branch_location'],
                    'payment_total':int(float(entry['payment_total'])*100),
                    'payment_type': entry['payment_type']
                })
            # split products to name and size
            prod_split = entry['product_name'].split(' ', 1)
            entry_product_size = prod_split[0]
            entry_product_name = prod_split[1]
            # Check if the product already exists in product_table
            product_exists = False
            for product in product_table:
                if product['name'] == entry_product_name and product['size'] == entry_product_size:
                    product_exists = True
                    break
            # Add new product if it's not already in product_table
            if not product_exists:
                product_table.append({
                    'product_id': product_id,
                    'name': entry_product_name,
                    'size': entry_product_size,
                    'price': int(float(entry['product_price'])*100)
                })
                product_id += 1
            
            # get product id for current record based on product_name and product_size
            for product in product_table:
                if product['name'] == entry_product_name and product['size'] == entry_product_size:
                    current_product_id = product['product_id']
                    break
            order_products.append({
                'order_id': order_id,
                'product_id': current_product_id
            })


        return order_table, product_table, order_products
    except KeyError as e:
        raise Exception(f"Key not found: {e}")
    except ValueError as e:
        raise Exception(f"Value error: {e}")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")
        
#Importing test data

from mock_data.mock_data_lists import list_of_dicts_2nf

#Data variable for tests and module imports

import collections
order_table, product_table, order_products = third_nf(list_of_dicts_2nf)

#Unit test functions

def test_product_size_name_seperate():
    first_product_name = 'Iced americano'
    first_product_size = 'Regular'
    assert (product_table[0]['name'], product_table[0]['size']) == (first_product_name, first_product_size)

def test_price_is_pence():
    penny_price_first_product = 215
    assert product_table[0]['price'] == penny_price_first_product

def test_no_repeat_order_id():
    happy_path = 1
    id_list = []
    for entry in order_table:
        id_list += [entry['order_id']]
    count = [id_list.count(i) for i in id_list]
    for result in count:
        assert result == happy_path

def test_no_duplicate_product_size_pairs():
    count = collections.Counter([tuple(d.items()) for d in product_table])
    values = count.values()
    for result in values:
        if result > 1:
            raise Exception("Duplicate product id in products table")









    