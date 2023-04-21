# Write your code here
def word_count(string):
    total = 1
    for x in string:
        if x == " ":
            total += 1
    return total