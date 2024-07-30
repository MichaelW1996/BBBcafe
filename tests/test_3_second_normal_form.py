#Function being tested

def second_nf(dict_list):
    try:
        for dict in dict_list:
            product = dict['order_details_string']
            product_list = product.split('-')
            product_name = '-'.join(product_list[0:-1]).strip()
            product_price = product_list[-1].strip()
            dict['product_name'] = product_name
            dict['product_price'] = product_price
            del dict['order_details_string']
        return dict_list
    except KeyError as e:
        raise Exception(f"Key not found: {e}")
    except ValueError as e:
        raise Exception(f"Value error: {e}")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")
    
#Importing mock data

from mock_data.mock_data_lists import list_of_dicts_1nf

#Data for the test functions

data = second_nf(list_of_dicts_1nf)

#Unit test functions

def test_price_consistency():
    reg_chai_latte_price = '2.30'
    x = 0
    for dict in data:
        if data[x]['product_name'] == "Regular Chai latte":
            assert data[x]['product_price'] == reg_chai_latte_price
        x += 1

def test_one_dict_per_product_in_order():
    happy_path = 3
    id_dicts_in_order_2 = []
    for indiv_dict in data:
        if indiv_dict['id'] == 2:
            id_dicts_in_order_2 += [2]
    count_of_dicts = (len(id_dicts_in_order_2))
    assert count_of_dicts == happy_path