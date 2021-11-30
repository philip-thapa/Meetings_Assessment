'''
Module to write into employee csv file
'''

import csv


def write_employee():
    '''
    Method to write into employee csv file
    '''
    rows = [
        ['121', '9:00', '18:00', '12:00-13:00', '10:00-10:45'],
        ['122', '9:20', '18:20', '12:00-13:00', '10:00-10:45'],
        ['123', '9:50', '18:50', '12:00-13:00', '11:00-11:45'],
        ['124', '10:00', '19:00', '12:00-13:00', '11:45-12:30'],
        ['125', '10:30', '19:30', '12:00-13:00', '12:30-13:15'],
        ['126', '9:00', '18:50', '12:00-13:00', '13:00-13:45'],
        ['127', '9:00', '18:50', '12:00-13:00', '16:00-16:45']]

    with open("Employess.csv", 'a') as emp:
        employee_appender = csv.writer(emp)
        employee_appender.writerows(rows)

    print("Writing into employees.csv completed successfully")
