
```markdown
# Web Login Brute Forcing

![Web Login Brute Forcing]

## Overview

The Web Login Brute Forcing script is a Python script that performs brute force attacks on a web login page by trying different combinations of usernames and passwords. It uses a wordlist of passwords to perform the brute force attack. The script sends HTTP POST requests to the target URL with different username and password combinations and checks for a specific response indicating a successful login.

## Requirements

- Python 3.x
- Requests library

## Installation

1. Clone the repository:

```shell
git clone https://github.com/Madhav-Sai/Web-brute.py.git
```

2. Navigate to the project directory:

```shell
cd web-login-brute-forcing
```

3. Install the required libraries:



## Usage

1. Update the script:

   - Set the `target` variable to the URL of the target login page.
   - Add the desired usernames to the `usernames` list.
   - Provide the path to the password wordlist file by updating the `passwords` variable.
   - Modify the `needle` variable to match the expected response indicating a successful login.

2. Run the script:

```shell
python web-brute.py
```

The script will attempt different combinations of usernames and passwords from the provided wordlist. It will send HTTP POST requests to the target URL with each combination and check for the expected response. If a successful login is detected, the valid credentials will be displayed.

Please note that brute forcing login pages without proper authorization is illegal and unethical. Only use this script on systems that you are authorized to test and ensure you have permission from the owner of the target system before running this script.


Please verify and update the necessary information, such as the target URL, usernames, wordlist file path, and expected response, to match your specific use case.
