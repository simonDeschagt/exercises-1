# Write your code here
import re

def zero_or_more_abc(string):
    return re.fullmatch("(abc){,}", string)
#  of return re.fullmatch("(abc)*", string ) is ook correct