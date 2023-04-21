# Write your code here
def median(n):
    n.sort()
    if len(n)%2 == 0:
        return (n[int(len(n)/2)] + n[int(len(n)/2-1)]) /2
    return n[int((len(n)-1)/2)]