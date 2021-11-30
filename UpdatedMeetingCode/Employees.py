'''
Module to call the sub employee modules
'''
from create_employee import create_employee
from write_employee import write_employee
from meeting_availability import check_meeting_availability


def employees():
    '''
    main method to call the imported modules
    '''
    while True:
        user_input = int(input(
            "Enter the option \n1: create Employee \n2: Write into employees \n3: Check Meeting meeting Availability "
            "\n4: Break \n"))
        if user_input == 1:
            create_employee()
        elif user_input == 2:
            write_employee()
        elif user_input == 3:
            check_meeting_availability()
        elif user_input == 4:
            break
        else:
            print("INVALID OPTION")


employees()
