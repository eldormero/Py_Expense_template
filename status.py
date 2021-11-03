from PyInquirer import prompt
import csv


# Get user from the csv file users.csv and return a list of users
def get_user():
    with open('users.csv', newline='') as f:
        reader = csv.reader(f)
        l = []
        for row in reader:
            l.append(row[0])
        return l

def get_status():
    l = get_user()
    for i in l:
        print(i + " owes nothing")
    return True