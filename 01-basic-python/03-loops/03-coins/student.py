# Write your code here
def coins(one, two, five, goal):
    while goal >= 5 and five > 0:
        goal -= 5
        five -= 1
    while goal >= 2 and two > 0:
        goal -= 2
        two -= 1
    while goal >=1 and one > 0:
        goal -= 1
        one -= 1
    if goal == 0:
        return True
    return False