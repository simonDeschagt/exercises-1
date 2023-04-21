# Write your code here
import re

def correct_dates(string):
    return re.sub(r'(\d+)/(\d+)', r'\2/\1', string)