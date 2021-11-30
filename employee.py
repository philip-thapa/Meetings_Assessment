# Assesment Test
# Create a module named Meetings,
# Build a functionality of creating, reading , updating csv files of Data consisting
# 1. Employee , in time, out-time , break time,  2. employee, meetings.
# Write alogorithm to fecth available meeting time of requested time interval.
# If Meeting avalable update their respective record in csv.
# Write few test cases on creation updating, fecthing and quering of csv records.	
'''
module to call create, write, read and update method of employee
'''

from test_creation_employee_csv import test_create_employee_csv
from test_reading_employee_csv import test_read_from_csv_file
from test_updating_employee_csv import update_epmoyee_csv
from test_writing_employee_csv import test_writing_into_csv


def employee_meeting():
    '''
    method to call create, read, write and update
    '''
    while True:
        user_input = int(input(
            "Choose the option: \n1: create employee.csv \n2: write into employee.csv \n3: Read from employee.csv \n4: Update employee.csv \n5: break\n"))
        if user_input == 1:
            test_create_employee_csv()
            print("Employee_meeting.csv created SUCCESSFULLY")
        elif user_input == 2:
            test_writing_into_csv()
            print("Writing Successful")
        elif user_input == 3:
            test_read_from_csv_file()
        elif user_input == 4:
            update_epmoyee_csv()
        elif user_input == 5:
            break
        else:
            print("Please enter valid option")


employee_meeting()
