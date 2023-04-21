# Write your code here
import re

def is_valid_password(string):
    return re.fullmatch(r'[0-9a-zA-Z\*\-\+\/\.\@]{12}', string)