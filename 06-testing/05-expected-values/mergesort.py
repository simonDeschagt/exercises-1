def split_in_two(ns):
    middle = len(ns) // 2
    left = ns[:middle]
    right = ns[middle:]
    return (left, right)

def merge_sorted(left, right):
    left_counter = 0
    right_counter = 0
    result = list()
    while (left_counter < len(left) and right_counter < len(right)):
        if (left[left_counter] < right[right_counter]):
            result.append(left[left_counter])
            left_counter += 1
        else:
            result.append(right[right_counter])
            right_counter += 1

    if (left_counter < len(left)):
        for x in left[left_counter:]:
            result.append(x)
    elif (right_counter < len(right)):
        for x in right[right_counter:]:
            result.append(x)

    return result

def merge_sort(ns):
    if ns == []:
        return []
    left, right = split_in_two(ns)
    left.sort()
    right.sort()
    sorted_list = merge_sorted(left, right)
    return sorted_list