'''
Module to read the csv file
'''

import csv


def test_read_from_csv_file():
    '''
    Method to read the employee meeting csv file
    :return:
    '''
    try:
        with open('Employee_meeting.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader)
            # print("HEADER", header)
            assert ['Employee Name', 'Date', 'In Time', 'Out Time',
                    'Break Time', 'Employee Meeting'] == header

            for line in csv_reader:
                print("On " + line[1] + " " + line[0] + " In time was " + line[2] + " out time was " +
                      line[3] + " break time was "+line[4] + " and employee meeting was " + line[5])
    except NameError:
        print("File not found")
    except:
        print("Something went wrong")
    finally:
        csv_file.close()


# test_read_from_csv_file()
