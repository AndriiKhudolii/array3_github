def get_new_list_1(input_list):
    average_value = sum(input_list) / len(input_list)
    return [x * average_value for x in input_list]
