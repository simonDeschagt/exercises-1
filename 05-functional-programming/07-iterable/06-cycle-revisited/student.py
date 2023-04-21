def cycle(values):
    # If values is an iterator, we need to make a copy
    values = list(values)
    while True:
        for value in values:
            yield value

values = list("abc")
for x in range(4):
    for value in values:
        print(value)