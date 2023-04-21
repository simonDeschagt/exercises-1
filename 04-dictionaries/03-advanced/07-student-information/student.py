# Write your code here
def process_data(lijstje):
    students = {}
    for item in lijstje:
        naam, age, *courses = item.split(",")
        students[naam] = {
                'age': int(age),
                'courses': courses
            }
    # print(students)
    return students

# process_data(["gay,20,en,gasd","lessgay,201,nl,adfa,adfa"])

def average_age(data):
    students = process_data(data)
    print(students)
    # total_age = 0
    # for x in students:
    #     total_age += x[0]
average_age(["gay,20,en,gasd"+"\n","lessgay,201,nl,adfa,adfa"])