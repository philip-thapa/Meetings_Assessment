'''
Module to read the csv file
'''

import csv


def read_employess_from_csv():
    '''
    Method to read the employee meeting csv file
    '''
    try:
        with open('Employess.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for line in csv_reader:
                print("Employee Id "+line[0]+" in time is "+line[1]+" out time is " +
                      line[2]+" Break time is "+line[3]+" and meeting time slot is "+line[4])
    except NameError:
        print("File not found")
    except:
        print("Something went wrong")


# test_read_from_csv_file()
