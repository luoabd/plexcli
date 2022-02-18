from account import Account
from prompts import Prompts

# User login
account = Account.login()

# Choose server
resource = Prompts.get_servers(account)