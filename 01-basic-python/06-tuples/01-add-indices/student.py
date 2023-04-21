# Write your code here
def add_indices(lijst):
    new_lijst = list()
    for x in range(0, len(lijst)):
        new_lijst.append(x)
    return list(zip(new_lijst, lijst))