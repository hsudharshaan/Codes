#filename : ex35-manip-strings
# checking for numbers in a string
# loop untill user enter pin

s = 'a'

while(not(1.isdecimal())):
    s = input('enter pin: ')

print('thats a good number')