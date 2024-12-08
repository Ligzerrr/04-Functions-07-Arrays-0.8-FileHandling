###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
import keyinput # your own defined module

# Reads employee's data from keyboard
first_name = keyinput.input_string('Enter your name: ')
last_name = keyinput.input_string('Enter your last name: ')
age = keyinput.input_integer('Enter your age: ')
salary = keyinput.input_real('Enter your salary: ')
is_salary_hidden = keyinput.input_boolean('Hide salary? (y/n): ')

# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name: ', first_name)
print('Last: ', last_name)
print('Age: ', age)
if not is_salary_hidden:
    print('Salary: ',salary)