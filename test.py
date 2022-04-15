# Variables
students_count = 1000
rating = 4.99
is_published = True
course_name = "Python Programming"
print(students_count)
message = """
Hi

This is Krishnan from RBC

Regards
Krishnan
"""
print(message)
course = "Python Programming"
print(len(course))
print(course[5:10])  # print 5th character to 9th Character
print(course[0:])  # print the complete string from 0 character
print(course[:])  # print the complete string from 0 character
print(course[:len(course)])  # print the complete string from 0 character
print(course[-1])  # the negative will print the last character
# For the below Example In between we are putting " so that we have prefix with Escape character \"
# \"
# \'
# \\
# \n
course = "Python \"Programming"
print(course)
course = "Python \'Programming"
print(course)
course = "Python \\Programming"
print(course)
course = "Python \nProgramming"
print(course)
print(course)

# Concatenation
First = "Krishnan"
Last = "Sampath"
name = First + "  " + Last
print(name)
# Formatted output
First = "Krishnan"
Last = "Sampath"
name = f"{Last} {First}"
print(name)

First = "Shrivathsan"
output = f"{len(First)} {5*30}"
print(output)
output = f"{First} {5*30}"
print(output)
