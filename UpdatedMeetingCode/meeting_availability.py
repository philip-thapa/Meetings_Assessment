'''
Module to check meeting availability
If available it will append into the csv file of that particular employees
'''

import csv


def check_meeting_availability():
    with open("Employess.csv", 'r') as emp:
        user_input_employee1_id = input("Enter the ID of employee 1: ")
        user_input_employee2_id = input("Enter the ID of employee 2: ")

        employee1_meeting_time = None
        employee2_meeting_time = None

        employee_found_flag = False

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
                employee_found_flag = True

                splitted_epmloyee1_time = employee1_meeting_time.split("-")
                splitted_epmloyee2_time = employee2_meeting_time.split("-")
                employee1__start = splitted_epmloyee1_time[0].split(":")
                employee1_start_hour = employee1__start[0]
                employee1_start_min = employee1__start[1]
                employee1_end = splitted_epmloyee1_time[1].split(":")
                employee1_end_hour = employee1_end[0]
                employee1_end_min = employee1_end[1]

                employee2_start = splitted_epmloyee2_time[0].split(":")
                employee2_start_hour = employee2_start[0]
                employee2_start_min = employee2_start[1]
                employee2_end = splitted_epmloyee2_time[1].split(":")
                employee2_end_hour = employee2_end[0]
                employee2_end_min = employee2_end[1]

                if (employee1_end_hour < employee2_start_hour) or (employee1_end_hour == employee2_start_hour and employee1_end_min <= employee2_start_min) or (employee2_start_hour > employee1_end_hour) or (employee2_start_hour == employee1_end_hour and employee2_start_min >= employee1_end_min):
                    new_meeting_time_slot = input(
                        "Enter the new meeting time slot: ")

                    new_meeting_time_slot_splitted = new_meeting_time_slot.split(
                        "-")
                    # [12:00, 12:45]
                    new_meeting_start = new_meeting_time_slot_splitted[0]
                    new_meeting_end = new_meeting_time_slot_splitted[1]
                    new_meeting_start_splitted = new_meeting_start.split(":")
                    new_meeting_start_hour = new_meeting_start_splitted[0]
                    new_meeting_start_min = new_meeting_start_splitted[1]
                    new_meeting_end_splitted = new_meeting_end.split(":")
                    new_meeting_end_hour = new_meeting_end_splitted[0]
                    new_meeting_end_min = new_meeting_end_splitted[1]

                    employee1_break_time = (lst[FIRST_EMPLOYEE_INDEX])[3]
                    employee2_break_time = row[3]

                    employee1_break_time_splitted = employee1_break_time.split(
                        "-")
                    employee2_break_time_splitted = employee1_break_time.split(
                        "-")

                    employee1_breaktime_start = employee1_break_time_splitted[0]
                    employee1_breaktime_end = employee1_break_time_splitted[1]

                    employee1_breaktime_start_splitted = employee1_breaktime_start.split(
                        ":")
                    employee1_breaktime_start_hour = employee1_breaktime_start_splitted[0]
                    employee1_breaktime_start_min = employee1_breaktime_start_splitted[1]

                    employee1_breaktime_end_splitted = employee1_breaktime_end.split(
                        ":")
                    employee1_breaktime_end_hour = employee1_breaktime_end_splitted[0]
                    employee1_breaktime_end_min = employee1_breaktime_end_splitted[1]

                    employee2_break_time_start_splitted = (
                        employee2_break_time_splitted[0]).split(":")
                    employee2_break_time_end_splitted = (
                        employee2_break_time_splitted[1]).split(":")

                    employee2_break_time_start_hour = employee2_break_time_start_splitted[0]
                    employee2_break_time_start_min = employee2_break_time_start_splitted[1]

                    employee2_break_time_end_hour = employee2_break_time_end_splitted[0]
                    employee2_break_time_end_min = employee2_break_time_end_splitted[1]

                    if new_meeting_start_hour == employee1_breaktime_start_hour or new_meeting_start_hour == employee2_break_time_start_hour:
                        print("Employee has a break time")
                    elif new_meeting_start_hour == employee1_breaktime_end_hour and new_meeting_start_min < employee1_breaktime_end_min:
                        print("Employee 1 has a break time")
                    elif new_meeting_start_hour == employee2_break_time_end_hour and new_meeting_start_min < employee2_break_time_end_min:
                        print("Employee 2 has a break time")
                    elif new_meeting_start_hour == employee1_end_hour and new_meeting_start_min < employee1_end_min:
                        print("New meeting overlaps employee1 previous meeting")
                    elif new_meeting_start_hour == employee2_end_hour and new_meeting_start_min < employee1_end_min:
                        print("New meeting overlaps employee2 previous meeting")
                    elif new_meeting_end_hour == employee1_start_hour and new_meeting_end_min > employee1_start_min:
                        print("New meeting overlaps employee1 previous meeting")
                    elif new_meeting_end_hour == employee2_start_hour and new_meeting_end_min > employee2_start_min:
                        print("New meeting overlaps employee2 previous meeting")
                    else:
                        row[4] = row[4] + "," + new_meeting_time_slot

                        (lst[FIRST_EMPLOYEE_INDEX])[4] = (
                            lst[FIRST_EMPLOYEE_INDEX])[4] + "," + new_meeting_time_slot

                else:
                    print("Employee " + user_input_employee1_id + " and Employee " +
                          user_input_employee2_id+" Meeting Slot overlap with each other")
                employee1_meeting_time = None
                employee2_meeting_time = None
            lst.append(row)
        if not employee_found_flag:
            print("Employee ID not found")

        with open("Employess.csv", 'w') as emp:
            employe_writer = csv.writer(emp)
            employe_writer.writerows(lst)
