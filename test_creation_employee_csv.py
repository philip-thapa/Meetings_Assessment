import csv


def test_create_employee_csv():
    headers = ["Employee Name", "Date", "In Time",
               "Out Time", "Break Time", "Employee Meeting"]
    try:
        with open("Employee_meeting.csv", 'w') as emp:
            employee = csv.writer(emp)
            employee.writerow(headers)

    except Exception as e:
        print("Cannot create a employee csv file", e)
    emp.close()


# test_create_employee_csv()
