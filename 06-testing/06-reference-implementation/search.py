def linear_search(students, target_id):
    for student in students:
        if student.id == target_id:
            return student
    return None

def binary_search(students, target_id):
    left = 0
    right = len(students)
    while left < right:
        mean = (left + right) // 2
        middle_id = students[mean].id
        if target_id > middle_id:
            left = mean + 1
        elif target_id < middle_id:
            right = mean
        else:
            return students[mean]
    return None
        
#     while left < right:
#         middle = (left + right) // 2
#         middle_id = students[middle].id
#         if id < middle_id:
#             right = middle
#         elif id > middle_id:
#             left = middle + 1
#         else:
#             return students[middle]
#     return None