#Function being tested

def first_nf(dict_list):
    output_dict_list = []   
    try:
        for dict in dict_list:
            product_list = dict['order_details_string'].split(',') 
            dict['order_details_string'] = product_list
            for product in product_list:
                new_dict = dict.copy()
                new_dict['order_details_string'] = product
                output_dict_list.append(new_dict)
        return output_dict_list
    except KeyError as e:
        raise Exception(f"Key not found: {e}")
    except ValueError as e:
        raise Exception(f"Value error: {e}")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

#Mock data before first normal form

from mock_data.mock_data_lists import list_of_dicts

#Output data varible used for both tests

output_dict_list = first_nf(list_of_dicts)

#Unit test functions

def test_indiv_dict_per_product():
    total_individual_projects = 27
    assert len(output_dict_list) == total_individual_projects

def test_orders_in_product_seperated():
    for indiv_dict in output_dict_list:
        if ',' in indiv_dict['order_details_string']:
            raise Exception('Order products not correctly seperated')


