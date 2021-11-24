import csv
from os import write

# def update_epmoyee_csv():

#     with open('Employee_meeting.csv', 'r') as emp:
#         reader = csv.reader(emp)
#         user_input_to_update = input("Enter the day: ")
#         found = False
#         lst = []
#         new_out_time = None
#         # header = next(reader)
#         for row in reader:
#             if row[1] == user_input_to_update:
#                 found = True
#                 new_out_time = input("Enter new out time: ")
#                 row[3] = new_out_time
#             lst.append(row)

#         if found:
#             with open('Employee_meeting.csv', 'w+') as emp:
#                 writer = csv.writer(emp)
#                 writer.writerows(lst)
#                 print("Successfully updated")
#         else:
#             print("Date not found")


def update_epmoyee_csv():
    try:
        updating_field_input = int(input(
            "Select the option from below to update: \n 1. In time \n 2. Out Time \n 3.Break Time \n"))
        date = input("Enter the date: ")
        lst = []
        found = False
        with open("Employee_meeting.csv", 'r') as emp:
            reader = csv.reader(emp)
            for row in reader:
                # print(type(row[1]), "  ", type(date))
                if row[1] == date:
                    # print("I am inside")
                    if updating_field_input == 1:
                        new_in_time = input("Enter the new In time: ")
                        row[2] = new_in_time
                        found = True
                    elif updating_field_input == 2:
                        new_out_time = input("Enter the new out time: ")
                        row[3] = new_out_time
                        found = True
                    elif updating_field_input == 3:
                        new_break_time = input("Enter the new break time: ")
                        row[4] = new_break_time
                        found = True
                lst.append(row)

            if found:
                with open("Employee_meeting.csv", "w") as emp:
                    writer = csv.writer(emp)
                    writer.writerows(lst)
                    print("Successfully updated")
            else:
                print("Invalid data provided")
    except:
        print("Something went wrong")


update_epmoyee_csv()
