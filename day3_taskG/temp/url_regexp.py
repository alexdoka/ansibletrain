#! /usr/bin/env python
import re
import requests

def remove_tags(text):
    TAG_RE = re.compile(r'<[^>]+>')
    TAG_N = re.compile(r'\\n')
    TAG_BR = re.compile(r'{(.*)}')
    res = TAG_RE.sub('', text)
    res = TAG_N.sub('', res)
    res = TAG_BR.sub('', res)
    return res

# def match_exp(urllink, pattern):
#     r = requests.get(urllink)
#     outstr = remove_tags(str(r.content))
#     return "Pattern was found" if re.match(pattern, outstr) else "Pattern was NOT found"

def match_exp(urllink, pattern):
    r = requests.get(urllink)
    outstr = remove_tags(str(r.content))
    return "Pattern was found" if re.search(pattern, outstr) else "Pattern was NOT found"

urllink = "http://localhost"
pattern = "allow"
sss = match_exp(urllink, pattern)
print(sss)

print(1)
