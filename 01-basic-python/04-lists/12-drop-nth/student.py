# Write your code here
def drop_nth(xs, n):
    new_list = xs[:n] + xs[n+1:]
    return new_list