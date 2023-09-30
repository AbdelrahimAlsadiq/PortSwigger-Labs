# OS Command Injection

### Lab 1: OS command injection, simple case.
- Intercept and modify a request that checks the stock.
- Modify the `storeID` parameter, giving it the value `1|whoami`.
- Observe that the response contains the name of the current user.

### Lab 2: Blind OS command injection with time delays.
- Intercept and modify the request that submits feedback.
- Modify the `message` parameter, changing it to `" & sleep 10 #`
- Observe that the response takes 10 seconds to return.

