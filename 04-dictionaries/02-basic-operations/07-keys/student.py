# Write your code here
def keys(dicti):
    print(list(dicti.keys()))
    return list(dicti)

list(dicti) == list(dicti.keys())# waarschijnelijk is er een vershil in type, maar hier is niets op aan te merken in de oefening

keys({'a': 1, 'b': 2})