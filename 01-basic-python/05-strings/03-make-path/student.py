# Write your code here
def make_path(parts):
    path = ""
    for x in parts:
        path += f'{x}/'
    return path[:len(path)-1]