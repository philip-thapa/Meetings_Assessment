import csv


def test_create_meeting_available_details():
    headers = ["Meeting Date", "Availability"]
    with open("meeting_availability_details.csv", 'w') as mee:
        meeting = csv.writer(mee)
        meeting.writerow(headers)
    mee.close()


test_create_meeting_available_details()
