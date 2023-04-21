from itertools import pairwise

def total_distance(path, distance):
    path_pairwise_list = list(pairwise(path))
    return sum(distance(x[0], x[1]) for x in path_pairwise_list)

