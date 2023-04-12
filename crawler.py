from pystyle import Anime, Write, Colorate, Colors, Box, Center
import undetected_chromedriver as webdriver
from sys import platform
import requests
import time
import os

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
#Commented to run automatically
#input()

path = os.path.abspath(os.path.dirname(__file__)) + "\chromedriver.exe"

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option,driver_executable_path=path)

for i in range(1, 1000):
    url = f"https://privatekeys.pw/keys/bitcoin/?page={i}"
    try:
        driver.get(url)
        time.sleep(1)
        while True:
            try:
                balance_value = (driver.find_element("xpath", '/html/body/main/div/div[2]/div[1]/h4/span/span[1]')).text.strip()
                break
            except:
                continue
        if float(balance_value) > 0:
            print(f"Balance found on page {i}: {balance_value}")
            with open("bitcoin_balances.txt", "a") as f:
                f.write(f"{url} {balance_value}\n")
                f.close()
        else:
            print(f"No balance found on page {i}.")
    except requests.exceptions.RequestException as e:
        print(f"Error accessing page {i}: {str(e)}")
