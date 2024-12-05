import hashlib

import requests


def requests_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"Error fetching: {response.status_code}, check the api and try again")
    return response


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = requests_api_data(first5_char)
    match = (line for line in response.text.splitlines() if line.split(":")[0] == tail)
    print(f"sh1: {sha1password}", "\n")
    print(f"tail: {tail}", "\n")
    for line in match:
        print(line, "\n")

    return response


pwned_api_check("123456")
