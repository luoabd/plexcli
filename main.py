from account import Account
from prompts import Prompts

# User login
account = Account.login()

# Choose server
# TODO: Integrate with config file
resource_name = Prompts.get_servers(account)
plex = account.resource(resource_name).connect()

# Initialize and start the navigation menu
menu = Prompts(plex)
menu.nav_menu()