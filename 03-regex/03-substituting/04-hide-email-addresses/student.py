# Write your code here
import re

def hide_email_addresses(string):
    def replace(match):
        new_string = ''
        m1 = match.groups()
        print(m1[0])
        for x in range(0,len(m1[0])):
            new_string += '*'
        return new_string
    return re.sub(r'([a-zA-Z\d.]+@[a-zA-Z\d.]+)', replace, string, flags=re.MULTILINE)

# hide_email_addresses("a@c.com")