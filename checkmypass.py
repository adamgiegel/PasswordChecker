import requests
import hashlib

def request_api_data(queryChar):
    url = 'https://api.pwnedpasswords.com/range/' + queryChar
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check api')
    return res

def get_password_leak_count(hashes, hashes_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hashes_to_check:
            return count
    return 0
    print(hashes)

def pwned_api_check(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_five_character = sha1_password[:5]
    second_part = sha1_password[5:]
    response = request_api_data(first_five_character)
    return get_password_leak_count(response, second_part)


def main(password):
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times')
        else:
            print("no")
        return "done!"

main('testing')