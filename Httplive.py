import requests
import argparse
from termcolor import colored
import time
print(colored("""

  _  _ _   _          _ _         
 | || | |_| |_ _ __  | (_)_ _____ 
 | __ |  _|  _| '_ \ | | \ V / -_)
 |_||_|\__|\__| .__/ |_|_|\_/\___|
              |_|  
              
#C0ded By Red Virus                                             
""","red"))
parser = argparse.ArgumentParser("""
Live    : Check If Url Up Or Down
ex:python3 Httplive.py --live http://google.com
""")
parser.add_argument("-Live","--Live")
args = parser.parse_args()
url = args.Live
def httplive(url):
    try:
        req = requests.get(url)
        if req.status_code == 200:
            print(colored("Http Live: ","green"),url)
    except requests.exceptions.ConnectionError:
        print(colored("Http Down: ","red"),url)
if url !=None:
    print("Please Wait ...")
    time.sleep(3)
    httplive(url)