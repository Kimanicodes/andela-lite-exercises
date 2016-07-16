from datetime import datetime

student = {'Name_Details': ['Kimani', 'Ndegwa'],
           'Year of Birth': datetime(1994, 5, 15),
           'Phone Number': '0726114094'}

'''Print Last Name Only: First Method'''
names = student['Name_Details']
print ("Last Name: " + names[1])
'''Print Last Name Only: Second Method'''
print ("Last Name: " + student['Name_Details'][1])
'''Remaining Exercises'''
print('My names are ' + str(student['Name_Details']))
print(student['Year of Birth'])
print(student['Phone Number'])
