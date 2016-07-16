from datetime import datetime

student = {'Name_Details': ['Kimani', 'Ndegwa'],
           'Year of Birth': datetime(1994, 5, 15),
           'Phone Number': '0726114094'}

'''Print Last Name Only'''
names = student['Name_Details']
print ("Last Name: " + names[1])
print(student.get('Name_Details.get(1)'))
print('My names are ' + str(student['Name_Details']))
print(student['Year of Birth'])
print(student['Phone Number'])
