from pystyle import Anime, Write, Colorate, Colors, Box, Center
from sys import platform
import requests

def header():
    print(Center.XCenter(Colorate.Vertical(Colors.purple_to_red, """
    $$$$$$\                   $$$$$$\                                   $$\                     
    $$  __$$\                 $$  __$$\                                  $$ |                    
    \__/  $$ |$$\   $$\       $$ /  \__| $$$$$$\  $$$$$$\  $$\  $$\  $$\ $$ | $$$$$$\   $$$$$$\  
     $$$$$$  |\$$\ $$  |      $$ |      $$  __$$\ \____$$\ $$ | $$ | $$ |$$ |$$  __$$\ $$  __$$\ 
    $$  ____/  \$$$$  /       $$ |      $$ |  \__|$$$$$$$ |$$ | $$ | $$ |$$ |$$$$$$$$ |$$ |  \__|
    $$ |       $$  $$<        $$ |  $$\ $$ |     $$  __$$ |$$ | $$ | $$ |$$ |$$   ____|$$ |      
    $$$$$$$$\ $$  /\$$\       \$$$$$$  |$$ |     \$$$$$$$ |\$$$$$\$$$$  |$$ |\$$$$$$$\ $$ |      
    \________|\__/  \__|       \______/ \__|      \_______| \_____\____/ \__| \_______|\__|      
                                                                                             
                                                                                             
    """)))

header()
input()

for i in range(1, 1000):
    url = f"https://privatekeys.pw/api/balance/bitcoin/{i}"
    try:
        res = requests.get(url)
        balance_value = res.json()['balance']
        if float(balance_value) > 0:
            print(f"Balance found on page {i}: {balance_value}")
            with open("bitcoin_balances.txt", "a") as f:
                f.write(f"{url} {balance_value}\n")
        else:
            print(f"No balance found on page {i}.")
    except requests.exceptions.RequestException as e:
        print(f"Error accessing page {i}: {str(e)}")
