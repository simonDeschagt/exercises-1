# Write your code here
import re

def only_vowels(string):
    return re.fullmatch("(a|e|o|i|u|)*", string)
