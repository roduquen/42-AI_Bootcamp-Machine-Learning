import sys

list = [ x for x in sys.argv ]
str = " ".join(list)
print(str[::-1])
