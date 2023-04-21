# Write your code here
def last_digit(n):
    return n%10

def remove_last_digit(n):
    last = last_digit(n)
    n -= last
    n = n / 10
    return n

def digit_sum(n):
    total = 0
    while n > 0:
        total += last_digit(n)
        n = remove_last_digit(n)
    return total