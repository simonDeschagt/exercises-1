# Write your code here
def includes(xs, ys):
    sxs = set()
    sys = set()
    for x in xs:
        sxs.add(x)
    for y in ys:
        sys.add(y)
    return sys.issubset(sxs)
