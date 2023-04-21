# Write your code here
import re

def is_dna(string):
    return re.fullmatch("(A|G|T|C)*", string)