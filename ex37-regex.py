#filename : ex37-regex
# use regex

import re

os = input("enter a class : ")

cfc = re.match('[/d][/D]',os)

if(cfc == None):
    print("that is not a class")
else:
    print("its a class")

