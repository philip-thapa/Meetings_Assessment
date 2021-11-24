import csv


def test_create_employee_csv():
    headers = ["Employee Name", "Date", "In Time",
               "Out Time", "Break Time", "Employee Meeting"]
    try:
        with open("Employee_meeting.csv", 'w') as emp:
            employee = csv.writer(emp)
            employee.writerow(headers)
            emp.close
            return headers

    except:
        print("Cannot create a employee csv file")

# test_create_employee_csv()
