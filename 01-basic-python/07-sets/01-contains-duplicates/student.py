# Write your code here
def contains_duplicates(xs):
    S = set()
    for x in xs:
        S.add(x)
    
    if len(S) == len(xs):
        return False
    return True