# Write your code here
def keys_with_value(dicti, value):
    return_list = list()
    for k,v in dicti.items():
        if v == value:
            return_list.append(k)
    return return_list