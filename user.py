from PyInquirer import prompt
user_questions = [
    {
        "type":"input",
        "name":"Name",
        "message":"New user - Name: ",
    },
]

def add_user():
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)
    print("User Added !")
    return True