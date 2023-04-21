class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def age(self):
        return self.age

def age(person):
    return person.age

def group_by(xs, key_function):
    result = {}
    for x in xs:
        key = key_function(x)
        if key in result:
            result[key].append(x)
        else:
            result[key] = []
            result[key].append(x)
    return result

print(group_by([Person(name="John", age=14),Person(name='Marc', age=17),
    Person(name='Sophie', age=15),
    Person(name='Chris', age=17),
    Person(name='Morgan', age=15),
], age)

)