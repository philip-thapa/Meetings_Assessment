import csv


def create_employee_details():
    try:
        headers = ['Id', "Employee Name", "Phone Number"]

        with open("EmployeeList.csv", 'w') as emp:
            csv_writer = csv.writer(emp)
            csv_writer.writerow\
                (headers)
    except:
        print("Something went wrong")


def write_empyee_details():
    field_names = ['Id', "Employee Name", "Phone Number"]

    test_case_1 = [
        {"Id": "121", "Employee Name": 'Ram', "Phone Number": '+91900'}]
    test_case_2 = [
        {"Id": "122", "Employee Name": 'Shyam', "Phone Number": '+91000'}]
    test_case_3 = [
        {"Id": "123", "Employee Name": 'Hari', "Phone Number": '+91890'}]
    test_case_4 = [
        {"Id": "124", "Employee Name": 'John', "Phone Number": '+91999'}]
    with open("EmployeeList.csv", 'a') as emp:
        csv_writer = csv.DictWriter(emp, fieldnames=field_names)
        csv_writer.writerows(test_case_1)
        csv_writer.writerows(test_case_2)
        csv_writer.writerows(test_case_3)
        csv_writer.writerows(test_case_4)


def fetch_employee_details():
    try:
        user_id_input = input("Enter the User Id: ")
        found = False
        with open("EmployeeList.csv", 'r') as emp:
            csv_reader = csv.reader(emp)
            next(csv_reader)
            for row in csv_reader:
                if int(row[0]) == user_id_input:
                    print("User Id " + row[0] + " " + "name is " + " " +
                          row[1] + " and Phone number is " + row[2])
                    found = True
            if not found:
                print("User Id not found")

    except:
        print("Something went wrong")


def fetch_details():
    while True:
        user_option = int(
            input("Enter \n1: Create a Employee List \n2: Write Employee details \n3: Fetch Details \n4: Break \n"))
        if user_option == 1:
            create_employee_details()
        elif user_option == 2:
            write_empyee_details()
        elif user_option == 3:
            fetch_employee_details()
        elif user_option == 4:
            break


fetch_details()


#
# Create a module named Meetings,
# Build a functionality of creating, reading , updating csv files of Data consisting
# 1. Employee , in time, out-time , break time,
# 2. employee, meetings. Write alogorithm to fecth available meeting time of requested time interval.
# If Meeting avalable update their respective record in csv. Write few test cases on creation updating,
# fecthing and quering of csv records.
