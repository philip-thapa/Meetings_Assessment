'''
Module to create a employee csv file
'''
import csv


def test_create_employee_csv():
    '''
    method to create a employee csv file
    '''
    headers = ["Employee Name", "Date", "In Time",
               "Out Time", "Break Time", "Employee Meeting"]
    try:
        with open("Employee_meeting.csv", 'w') as emp:
            employee = csv.writer(emp)
            employee.writerow(headers)
            emp.close()

    except FileNotFoundError:
        print("File not found")


# test_create_employee_csv()
