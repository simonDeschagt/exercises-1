# Write your code here
def remove_duplicates(xs):
    S = set()
    new_list = list()
    for x in xs:
        S.add(x)
        if len(S) != len(new_list):
            new_list.append(x)

    return new_list