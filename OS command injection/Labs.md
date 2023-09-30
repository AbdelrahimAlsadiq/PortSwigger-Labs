# OS Command Injection

### Lab 1: OS command injection, simple case.
- Intercept and modify a request that checks the stock.
- Modify the `storeID` parameter, giving it the value `1|whoami`.
- Observe that the response contains the name of the current user.
