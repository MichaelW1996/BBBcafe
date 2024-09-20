import csv

#Function being tested

def convert_csv(file):
    list_type= list()
    id = 0 
    try:
        for row in csv.DictReader(file, fieldnames = ['date_time', 'branch_location', 'customer_name', 'order_details_string', 'payment_total', 'payment_type', 'card_number']):
            row_cleaned = row
            row_cleaned['id'] = id
            del row_cleaned['card_number'] # remove card number field
            del row_cleaned['customer_name'] # remove name
            list_type.append(row_cleaned)
            id += 1
        return list_type
        #Try to catch common errors then have a catchall for any other errors
    except KeyError as e:
        raise Exception(f"Key not found: {e}")
    except ValueError as e:
        raise Exception(f"Value error: {e}")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")
        
#Testing that sensitive has been removed

mock_raw_data = open("tests/mock_data/raw_data.csv")

def test_card_number_removed():
    test_list = convert_csv(mock_raw_data)
    test_list_str = str(test_list)
    assert 'card_number' not in test_list_str

def test_customer_name_removed():
    test_list = convert_csv(mock_raw_data)
    test_list_str = str(test_list)
    assert 'customer_name' not in test_list_str

    

