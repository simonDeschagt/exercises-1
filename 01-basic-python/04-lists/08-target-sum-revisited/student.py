# Write your code here
def target_sum(ns, target):
    for x in ns:
        new_list = ns[:ns.index(x)] + ns[ns.index(x)+1:]
        for y in new_list:
            if x+y == target:
                return True
        for y in ns[x:]:
            if x+y == target:
                return True
    return False