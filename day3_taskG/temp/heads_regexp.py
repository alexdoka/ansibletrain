#! /usr/bin/env python
import re
import requests


def match_headers(str1, pattern1):
    return "Pattern was found" if re.match(pattern1, str1) else "Pattern was NOT found"

def get_site_headers(urllink):
    r = requests.get(urllink).headers
    server_info = ""
    for k in r:
        server_info = server_info + k +" "+ r[k]+ ", "
    return server_info[:-2]

hd = get_site_headers("http://localhost")
print(hd)
rrr = match_headers(hd, '(.*)nginx(.*)')

print(1)
