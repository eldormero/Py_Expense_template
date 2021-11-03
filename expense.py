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

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        'type': 'list',
        "name":"spender",
        "message":"New Expense - Spender: ",
        # Select a user between the different existant user in the users.csv file
        "choices": get_user()
    },

]



def add_to_csv(*args):
    with open('expense_report.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(args)

def new_expense(*args):
    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    add_to_csv(infos)
    return True


