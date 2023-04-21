def merge_dictionaries(d1, d2, merge_function):
    merged_dict = dict(d1)
    for y, z in d2.items():
        # print(y)
        if y in merged_dict:
            merged_dict[y] = merge_function(merged_dict[y], z)
        else:
            merged_dict[y] = z
    return merged_dict

# merge_dictionaries({"a":1, "b":2},{"c":1, "d":2}, "dd" )