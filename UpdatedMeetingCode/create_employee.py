'''
Module to create the employees csv file
'''

import csv


def create_employee():
    '''
    method to create employee csv file
    :return:
    '''
    headers = ['Id', 'In-Time', 'Out-Time', 'Break-Time', 'Meeting Time']
    with open("Employess.csv", mode='w') as emp:
        employee_create = csv.writer(emp)
        employee_create.writerow(headers)
    print("Employees.csv created successfully")
