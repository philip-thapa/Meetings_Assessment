import csv


def test_fetch_meeting_details(start_duration_time, end_duration_time, date):
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
                if (int((row[5])[:2]) >= int(start_duration_time) and int((row[5])[:2]) <= int(end_duration_time)) or (int((row[5])[:2]) <= int(start_duration_time) and int((row[5])[:2]) >= int(end_duration_time)):
                    # if (int(start_duration_time) >= 1 and int(end_duration_time) <= 7 and int((row[5])[:2]) >= int(start_duration_time) and int((row[5])[:2]) <= int(end_duration_time)) or (int(start_duration_time) >= 10 and int(end_duration_time) <= 12 and int((row[5])[:2]) >= int(start_duration_time) and int((row[5])[:2]) <= int(end_duration_time)):
                    with open("meeting_availability_details.csv", 'a') as mee:
                        field_name = ["Meeting Date", "Availability"]
                        Dict = {"Meeting Date": date, "Availability": "Yes"}
                        appender = csv.DictWriter(mee, fieldnames=field_name)
                        appender.writerow(Dict)
                        mee.close()
                        return True
                else:
                    with open("meeting_availability_details.csv", 'a') as mee:
                        field_name = ["Meeting Date", "Availability"]
                        Dict = {"Meeting Date": date, "Availability": "No"}
                        appender = csv.DictWriter(mee, fieldnames=field_name)
                        appender.writerow(Dict)
                        mee.close()
                        return False

    emp.close()


def test_fetch_meeting_details():
    assert True == fetch_meeting_details(1, 7, "01 Nov 21")
    assert True == fetch_meeting_details(1, 7, "02 Nov 21")
    assert False == fetch_meeting_details(4, 7, "03 Nov 21")
