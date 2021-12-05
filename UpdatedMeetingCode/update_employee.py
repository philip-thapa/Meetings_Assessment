'''
module to update the in time, out time and break time
'''

import csv


def update_epmoyee_csv():
    '''
    method to update the in time, out time and break time of an employee
    '''

    try:
        updating_field_input = int(input(
            "Select the option from below to update: \n 1. In time \n 2. Out Time \n 3. Break Time \n"))
        employee_Id = input("Enter the Employee ID: ")
        lst = []
        found = False
        with open("Employess.csv", 'r') as emp:
            reader = csv.reader(emp)
            for row in reader:
                if row[0] == employee_Id:
                    if updating_field_input == 1:
                        new_in_time = input("Enter the new In time: ")
                        row[1] = new_in_time
                        found = True
                    elif updating_field_input == 2:
                        new_out_time = input("Enter the new out time: ")
                        row[2] = new_out_time
                        found = True
                    elif updating_field_input == 3:
                        new_break_time = input("Enter the new break time: ")
                        row[3] = new_break_time
                        found = True
                lst.append(row)

            if found:
                with open("Employess.csv", "w") as emp:
                    writer = csv.writer(emp)
                    writer.writerows(lst)
                    print("Successfully updated")
            else:
                print("Invalid data provided")
    except:
        print("Something went wrong")


# update_epmoyee_csv()
