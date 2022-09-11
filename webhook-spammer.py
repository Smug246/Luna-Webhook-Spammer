# Coded with ❤ by Luna's Dev Team.

import sys
import time
import os
import requests
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'colorama'])

from colorama import Fore, init

class webhook_spam:
    def __init__(self):
        self.choice = int(input(f"{Fore.MAGENTA}Do you want to spam the webhook (1) or delete it? (2){Fore.RESET} >>> "))

        if self.choice not in [1,2]:
            print(f"{Fore.RED}Invalid Choice!") 
            str(input(f"{Fore.MAGENTA}Press anything to exit..."))
            sys.exit()

        if self.choice == 1:
            self.webhook = str(input(f"{Fore.MAGENTA}Webhook{Fore.RESET} >>> "))

            if not self.check_webhook(self.webhook): 
                print(f"{Fore.RED}Invalid Webhook!{Fore.RESET}")
                str(input(f"{Fore.MAGENTA}Press anything to exit..."))
                sys.exit()

            self.message = str(input(f"{Fore.MAGENTA}Message{Fore.RESET} >>> "))
            self.iterations = int(input(f"{Fore.MAGENTA}Iterations{Fore.RESET} >>> "))

            if self.iterations < 0:
                print(f"{Fore.RED}Invalid Iterations!{Fore.RESET}")
                str(input(f"{Fore.MAGENTA}Press anything to exit..."))
                sys.exit()

            self.spam_threads(self.webhook, self.inflate_message(self.message), self.iterations)

        if self.choice == 2:
            self.webhook = str(input(f"{Fore.MAGENTA}Webhook{Fore.RESET} >>> " ))
            print(f"{Fore.GREEN}Deleting Webhook!{Fore.RESET}")
            requests.delete(self.webhook)
            print(f"{Fore.GREEN}Webhook has been deleted!{Fore.RESET}") 
            str(input(f"{Fore.MAGENTA}Press anything to exit..."))
            sys.exit()

    def spam_threads(self, webhook, message, iterations):
        def spam(webhook, message):
            r = requests.post(
                webhook,
                json = {"content" : message}
            )
            
            if r.status_code == 204:
                print(f"{Fore.GREEN}Sent! | {r.status_code}\n{Fore.RESET}")
                
            elif r.status_code == 429:
                print(f"{Fore.RED}Rate Limit! | {r.status_code}\n{Fore.RESET}")
                return 429
                
            else:
                print(f"{Fore.YELLOW}{r.status_code}\n{Fore.RESET}")
                str(input(f"{Fore.MAGENTA}Press anything to exit..."))
                sys.exit()
                
        for x in range(iterations):
            for y in range(5):
                if spam(webhook, message) == 429:
                    time.sleep(5)
                
            time.sleep(5)
            
    def inflate_message(self, message):
        message = f"@everyone {message}\n"
        message = message * (999//len(message) + 1)
        return message
             
    def check_webhook(self, webhook):
        try:
            with requests.get(webhook) as r:
                if r.status_code == 200:
                    return True
                else:
                    return False
        except:
            return False
    
if __name__ == "__main__":
    init()
    
    if not os.name == "nt":
        os.system("clear")
    else:
        os.system("cls")
    
    try: webhook_spam()
    except KeyboardInterrupt: input(f"\n\n{Fore.YELLOW}KeyboardInterrupt: Exiting...{Fore.RESET}")
    except Exception as e: input(f"\n\n{Fore.RED}Error: {e}{Fore.RESET}")
