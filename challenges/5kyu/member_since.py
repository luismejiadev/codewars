#https://www.codewars.com/kata/scraping-get-the-year-a-codewarrior-joined/python


import re
from urllib.request import urlopen


def get_member_since(username):
    url = 'https://www.codewars.com/users/{0}'.format(username)
    info = str(urlopen(url).read())
    match = re.search('<div class="stat"><b>Member Since:</b>(.*?)</div>', info)
    return match.group(1) if match else 'Not Found'