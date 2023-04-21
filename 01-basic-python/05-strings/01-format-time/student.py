# Write your code here
def format_time(hours, minutes, seconds):
    if hours <10:
        hour = "0" + str(hours)
    else:
        hour = str(hours)
    if minutes <10:
        minute = "0" + str(minutes)
    else:
        minute = str(minutes)
    if seconds <10:
        sec = "0" + str(seconds)
    else:
        sec = str(seconds)
    return f'{hour}:{minute}:{sec}'