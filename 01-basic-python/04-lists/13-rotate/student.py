# Write your code here
def rotate(xs, n):
    for x in range(0,n):
        xs.append(xs.pop(0))
    return xs