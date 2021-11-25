'''
module to extract the meeting time of an employee and check whether he is available or not
'''
import csv


def fetch_meeting_details(start_duration_time, end_duration_time, date):
    '''
    method to check whether the employee is available for the meeting based on the given time interval
    Based on his availability Employee availability csv file will be updated
    '''
    with open("Employee_meeting.csv", 'r') as emp:
        reader = csv.reader(emp)
        next(reader)
        # start_duration_time = input(
        #     "Enter the start interval: ")
        # end_duration_time = input(
        #     "Enter the end interval: ")

        # date = input("Enter the date for the meeting: ")

        for row in reader:
            if row[1] == date:
                if (int(start_duration_time) <= int((row[5])[:2]) <= int(end_duration_time)) and (int((row[5])[:2]) != int((row[6])[:2])):
                    with open("meeting_availability_details.csv", 'a') as mee:
                        field_name = ["Meeting Date", "Availability"]
                        availability_details = {"Meeting Date": date, "Availability": "Yes"}
                        appender = csv.DictWriter(mee, fieldnames=field_name)
                        appender.writerow(availability_details)
                        mee.close()
                        return True
                else:
                    with open("meeting_availability_details.csv", 'a') as mee:
                        field_name = ["Meeting Date", "Availability"]
                        availability_details = {"Meeting Date": date, "Availability": "No"}
                        appender = csv.DictWriter(mee, fieldnames=field_name)
                        appender.writerow(availability_details)
                        mee.close()
                        return False

    emp.close()


def test_fetch_meeting_details():
    '''
    method to call fetch_meeting_details that either return true or false
    '''
    assert True == fetch_meeting_details(1, 7, "01 Nov 21")
    assert True == fetch_meeting_details(2, 7, "02 Nov 21")
    assert False == fetch_meeting_details(4, 7, "03 Nov 21")
    assert False == fetch_meeting_details(2, 3, "03 Nov 21")
    assert True == fetch_meeting_details(2, 4, "01 Nov 21")
