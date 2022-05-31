#filename : ex23-lists
#search for an item in a list



studentlists = ['arnav', 'rick', 'collete', 'ian']

box1 = input('enter students name to search : ')
if (box1 in studentlists):
    print('student is found.')
else:
    print('student is not found.')