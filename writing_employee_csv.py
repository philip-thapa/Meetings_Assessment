import csv


def test_writing_into_csv():
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

    test_case_1 = [{"Employee Name": "Philip", "Date": "01 Nov 21", "In Time": "9:30", "Out Time": "7:20", "Break Time": "2:00", "Employee Meeting": "3:00"}]
    test_case_2 = [{"Employee Name": "Philip", "Date": "02 Nov 21", "In Time": "9:40", "Out Time": "7:10", "Break Time": "2:00"}]
    test_case_3 = [{"Employee Name": "Philip", "Date": "02 Nov 21", "In Time": "9:40", "Out Time": "7:10", "Break Time": "2:00", "Employee Meeting": "3:30"}]
    fields = ["Employee Name", "Date", "In Time", "Out Time", "Break Time", "Employee Meeting"]
    filename = "Employee_meeting.csv"

    with open(filename, 'a') as emp:
        append_employee = csv.DictWriter(emp, fieldnames=fields)
        append_employee.writerows(test_case_1)
        assert len(test_case_1[0]) == 6
        assert [{"Employee Name": "Philip", "Date": "01 Nov 21", "In Time": "9:30", "Out Time": "7:20", "Break Time": "2:00", "Employee Meeting": "3:00"}] == test_case_1
        append_employee.writerows(test_case_2)
        assert  len(test_case_2[0]) == 5
        append_employee.writerows(test_case_3)
        assert len(test_case_3[0]) == 6
    emp.close()


test_writing_into_csv()


# Assesment Test	Create a module named Meetings, Build a functionality of creating, reading , updating csv files of Data consisting 1. Employee , in time, out-time , break time,  2. employee, meetings. Write alogorithm to fecth available meeting time of requested time interval. If Meeting avalable update their respective record in csv. Write few test cases on creation updating, fecthing and quering of csv records.	2