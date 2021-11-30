'''
Module to check meeting availability
If available it will append into the csv file of that particular employees
'''

import csv


def check_meeting_availability():
    '''
    Method to check for the availability of meeting
    Asks the user to input two employees Id and checks whether the time slot are contradicting
    If not contradicted it will append into the meeting slot of that particular employees
    '''
    with open("Employess.csv", 'r') as emp:
        user_input_employee1_id = input("Enter the ID of employee 1: ")
        user_input_employee2_id = input("Enter the ID of employee 2: ")

        employee1_meeting_time = None
        employee2_meeting_time = None

        lst = []
        employee_csv_reader = csv.reader(emp)
        for i, row in enumerate(employee_csv_reader):
            if row[0] == user_input_employee1_id:
                employee1_meeting_time = row[4]
                global FIRST_EMPLOYEE_INDEX
                FIRST_EMPLOYEE_INDEX = i
            elif row[0] == user_input_employee2_id:
                employee2_meeting_time = row[4]
            if employee1_meeting_time and employee2_meeting_time:

                splitted_epmloyee1_time = employee1_meeting_time.split("-")
                splitted_epmloyee2_time = employee2_meeting_time.split("-")
                # employee1__start = splitted_epmloyee1_time[0].split(":")
                # employee1_start_hour = employee1__start[0]
                # employee1_start_min = employee1__start[1]
                employee1_end = splitted_epmloyee1_time[1].split(":")
                employee1_end_hour = employee1_end[0]
                employee1_end_min = employee1_end[1]

                employee2_start = splitted_epmloyee2_time[0].split(":")
                employee2_start_hour = employee2_start[0]
                employee2_start_min = employee2_start[1]
                # employee2_end = splitted_epmloyee2_time[1].split(":")
                # employee2_end_hour = employee2_end[0]
                # employee2_end_min = employee2_end[1]

                if (employee1_end_hour < employee2_start_hour) or (employee1_end_hour == employee2_start_hour and employee1_end_min <= employee2_start_min) or (employee2_start_hour > employee1_end_hour) or (employee2_start_hour == employee1_end_hour and employee2_start_min >= employee1_end_min):
                    row[4] = employee1_meeting_time + "," + employee2_meeting_time
                    (lst[FIRST_EMPLOYEE_INDEX])[
                        4] = employee1_meeting_time + "," + employee2_meeting_time
                    # print("LIST: ", lst)
                else:
                    print("Employee "+ user_input_employee1_id +  " and Employee " + user_input_employee2_id+" Meeting Slot contradict with each other")
                employee1_meeting_time = None
                employee2_meeting_time = None
            lst.append(row)

        with open("Employess.csv", 'w') as emp:
            employe_writer = csv.writer(emp)
            employe_writer.writerows(lst)
