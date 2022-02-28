import inquirer


class Prompts():
    def __init__(self, plex):
        self.plex = plex

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
        server_names = [server.name for server in server_list]
        questions = [
            inquirer.List('server',
                          message="Which server do you want to connect to?",
                          choices=server_names,
                          ),
        ]

        answers = inquirer.prompt(questions)
        resource = answers['server']
        return resource

    def nav_menu(self):
        questions = [
            inquirer.List('menu',
                          message="What would you like to do?",
                          choices=[('Browse Libraries', 1),
                                   ('Continue watching', 2),
                                   ('On deck content', 3),
                                   ('Recently added media', 4),
                                   ('Exit', 0)]
                          ),
        ]
        answers = inquirer.prompt(questions)
        choice_menu = answers['menu']

        match choice_menu:
            case 1:
                self.browse_library_menu()
            case 2:
                print("continue_watching_menu")
            case 3:
                print("on_deck_menu")
            case 4:
                print("recently_added_menu")
            case 0:
                exit()

    def browse_library_menu(self):
        library_sections = self.plex.library.sections()
        section_names = [section.title for section in library_sections]
        section_names.append("<= Go back")
        questions = [
            inquirer.List('section',
                          message="Which library do you want to browse?",
                          choices=section_names,
                          ),
        ]
        answers = inquirer.prompt(questions)
        choice_section = answers['section']
        match choice_section:
            case "<= Go back":
                # TODO: go to previous menu
                exit()
            case _:
                self.browse_section_menu(choice_section)

    def browse_section_menu(self, choice_section):
        section = self.plex.library.section(choice_section)
        questions = [
            inquirer.List('menu',
                          message="What would you like to do?",
                          choices=[(f'Show all {section.type}s', 1),
                                   ('Browse by filter (Genre, language, ...)', 2),
                                   (f'Browse Recently added {section.type}s', 3),
                                   ('<= Go back', 0)]
                          ),
        ]
        answers = inquirer.prompt(questions)
        choice_menu = answers['menu']
        match choice_menu:
            case 1:
                self.show_all(section)
            case 2:
                self.show_available_filters(section)
            case 3:
                print("show_recently_added()")
            case 0:
                exit()

    def show_all(self, section):
        # TODO: Pagination
        all_media_names = [media.title for media in section.all()]
        all_media_names.append("<= Go back")
        questions = [
            inquirer.List('media',
                          message="Select a movie/show:",
                          choices=all_media_names,
                          ),
        ]
        answers = inquirer.prompt(questions)
        choice_media = answers['media']
        match choice_media:
            case "<= Go back":
                # TODO: go to previous menu
                exit()
            case _:
                streamable_url = section.get(choice_media).getStreamURL()
                return(streamable_url)