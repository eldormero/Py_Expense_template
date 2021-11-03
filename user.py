from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"Name",
        "message":"New user - Name: ",
    },
]

# Add users to a csv file (users.csv)
def add_to_csv(*args):
    with open('users.csv', 'a', newline='') as csvfile:
        user = []
        infos = args[0]
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quoting=csv.QUOTE_MINIMAL)
        for e in infos:
            user.append(infos[e])
        spamwriter.writerow([user[0]])

def add_user():
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)
    # Add user to CSV
    add_to_csv(infos)
    print("New User Added !")
    return True