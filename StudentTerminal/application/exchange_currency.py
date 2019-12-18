import requests

# Where USD is the base currency you want to use
# url = 'https://api.exchangerate-api.com/v4/latest/GBP'
#
# Making our request
# response = requests.get(url)
# data = response.json()
# will get from input
# target = "EUR"
# inputMoney = 50
# print(data.get('rates').get(target))


def conversion(base_cur, output_cur, amount):
    my_data = get_data_for_cur(base_cur)
    rate = my_data.get('rates').get(output_cur)
    return round(amount * rate, 2)


def get_data_for_cur(base_cur):
    base_url = "https://api.exchangerate-api.com/v4/latest/" + base_cur
    # Making our request
    cur_response = requests.get(base_url)
    data_cur = cur_response.json()
    return data_cur


# result = conversion("GBP", "TRY", 100)  # test to see if the functions work correctly
# print(result)
