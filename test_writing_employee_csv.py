'''
module to write into employee csv file
'''

import csv


def test_writing_into_csv():
    '''
    method to write into employee csv file
    '''
    # try:
    #     date = input("Enter the date: ")
    #     in_time = input("Enter In time: ")
    #     out_time = input("Enter out time: ")
    #     break_time = input("Enter break time: ")
    #     meeting_time = input("Enter meeting time: ")
    #     Dict = {"Employee Name": 'Philip', "Date": date, "In Time": in_time,
    #             "Out Time": out_time, "Break Time": break_time, "Employee Meeting": meeting_time}
    #     field_name = ["Employee Name", "Date", "In Time",
    #                   "Out Time", "Break Time", "Employee Meeting"]
    #     with open("Employee_meeting.csv", 'a') as emp:
    #         employee_writer = csv.DictWriter(emp, fieldnames=field_name)
    #         # employee_writer.writeheader()
    #         employee_writer.writerow(Dict)
    # except Exception as e:
    #     print("Something went wrong", e)
    #     emp.close()

    test_case_1 = [{"Employee Name": "Philip", "Date": "01 Nov 21", "In Time": "09:30",
                    "Out Time": "07:20", "Break Time": "02:00", "Employee Meeting": "03:00"}]
    test_case_2 = [{"Employee Name": "Philip", "Date": "02 Nov 21", "In Time": "09:40",
                    "Out Time": "07:10", "Break Time": "02:00", "Employee Meeting": "03:00"}]
    test_case_3 = [{"Employee Name": "Philip", "Date": "03 Nov 21", "In Time": "09:40",
                    "Out Time": "07:10", "Break Time": "02:00", "Employee Meeting": "01:00"}]
    test_case_4 = [{"Employee Name": "Philip", "Date": "04 Nov 21", "In Time": "09:42",
                    "Out Time": "07:11", "Break Time": "02:00", "Employee Meeting": "02:00"}]
    fields = ["Employee Name", "Date", "In Time",
              "Out Time", "Break Time", "Employee Meeting"]
    filename = "Employee_meeting.csv"

    with open(filename, 'a') as emp:
        append_employee = csv.DictWriter(emp, fieldnames=fields)
        append_employee.writerows(test_case_1)
        assert len(test_case_1[0]) == 6
        assert [{"Employee Name": "Philip", "Date": "01 Nov 21", "In Time": "09:30",
                 "Out Time": "07:20", "Break Time": "02:00", "Employee Meeting": "03:00"}] == test_case_1
        append_employee.writerows(test_case_2)
        assert len(test_case_2[0]) == 6
        append_employee.writerows(test_case_3)
        assert len(test_case_3[0]) == 6
        append_employee.writerows(test_case_4)
    emp.close()


# test_writing_into_csv()
