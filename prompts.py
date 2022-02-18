import inquirer

class Prompts():
    def __init__():
        None

    def get_credentials():
        questions = [
            inquirer.Text('username', message="Please enter your username"),
            inquirer.Password(
                'password', message="Please enter your password"),
        ]
        answers = inquirer.prompt(questions)
        username = answers['username']
        password = answers['password']
        return username, password