#filename : ex21-lists
#create a lucky draw program to pick a winner
#remove the student list in the previous excersise using remove()
#use pop()

import random

studentlists = ['arnav' , 'rick', 'collete', 'ian']

studentlists.remove('collete')
print(studentlists)
studentlists.pop(1)
print(studentlists)