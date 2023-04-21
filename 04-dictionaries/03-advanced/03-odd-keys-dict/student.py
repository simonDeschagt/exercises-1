# Write your code here
def odd_keys_dict(dicti):
    return {
        k: v
        for k, v in dicti.items()
        if k %2 != 0
    }