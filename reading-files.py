# read information

# employee_file = open("employees.txt",'r')
# print(employee_file.read())
# print(employee_file.readline())
# print(employee_file.readline())

# for  sentence in employee_file.readlines():
#     print(sentence)

# add information
# employee_file = open("employees.txt",'a')

# # employee_file.write('Toby - Human Resources')
# employee_file.write('\nKelly - Customer Service')

# overwriting existing file  or we can create a new file
employee_file = open("employees1.txt",'w')
employee_file.write('Toby - Human Resources')
employee_file.close()