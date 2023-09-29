# Path Traversal

### Lab 1: File path traversal, simple case.
- Open any image in the web page and intercept the request using `BurpSuite's Proxy`
- Change the filename parameter to `../../../etc/passwd`

### Lab 2: File path traversal, traversal sequences blocked with absolute path bypass.
- Open any image in the web page and intercept the request using `BurpSuite's Proxy`
- Change the filename parameter to `/etc/passwd`

