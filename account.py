import os.path
import configparser
import plexapi
from plexapi.myplex import MyPlexAccount

from prompts import Prompts

CONFIG_FILE = 'config.ini'
config = configparser.ConfigParser()

class Account():
    def login():
        first_iter = True
        while True:
            if(os.path.isfile(CONFIG_FILE) and first_iter):
                config.read(CONFIG_FILE)
                username = config['ACCOUNT']['username']
                password = config['ACCOUNT']['password']
                # servername = config['SERVER']['name']
            else:
                username, password = Prompts.get_credentials()
            try:
                account = MyPlexAccount(username, password)
                print("Successfully logged in!")
                print(f"Welcome {account.username}")
                return account
            except Exception as e:
                if isinstance(e, plexapi.exceptions.Unauthorized):
                    print("Wrong username or password! Please try again.")
                    first_iter = False
                elif isinstance(e, plexapi.exceptions.BadRequest):
                    print("You have performed too many requests, please try again after a while.")
                    break
                else:
                    print(f"Error: {type(e)}")
                    break
