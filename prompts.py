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

    def get_servers(account):
        server_list = account.resources()
        server_names = []
        for server in server_list:
            server_names.append(server.name)
        questions = [
            inquirer.List('server',
                          message="Which server do you want to connect to?",
                          choices=server_names,
                          ),
        ]

        answers = inquirer.prompt(questions)
        resource = answers['server']
        return resource