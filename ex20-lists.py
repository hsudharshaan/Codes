#filename : ex20-lists
#create a lucky draw program to pick a winner
#from the student list in the previous excersise

import random

studentlists = ['arnav' , 'rick', 'bob', 'collete', 'ian']

print('Congratulations! The luck winner is :')
print(studentlists[random.randint(0,3)])