#!/usr/bin/env python

from ansible.module_utils.basic import AnsibleModule
import psutil
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


def match_exp(urllink, pattern):
    r = requests.get(urllink)
    outstr = remove_tags(str(r.content))
    return \
        "Pattern '{}' was found in {}".format(pattern, urllink) \
            if re.match(pattern, outstr) else \
            "Pattern '{}' was NOT found in {}".format(pattern, urllink)


def find_procs_by_name(name):
    "Return a list of processes matching 'name'."
    ls = []
    for p in psutil.process_iter(attrs=['name']):
        if p.info['name'] == name:
            ls.append(p)
    res = []
    for i in ls:
        res.append({i.info['name']: i.pid})
    return res


def match_headers(str1, pattern1):
    return "Pattern was found" if re.match(pattern1, str1) else "Pattern was NOT found"


def get_site_headers(urllink):
    r = requests.get(urllink).headers
    server_info = ""
    for k in r:
        server_info = server_info + k + " " + r[k] + ", "
    return server_info[:-2]


def main():
    module = AnsibleModule(
        argument_spec=dict(
            process_name=dict(type='str'),
            urllink=dict(type='str'),
            pattern=dict(type='str'),
            pattern_for_headers=dict(type='str')
        )
    )
    proc_name = module.params["process_name"]
    urllink = module.params["urllink"]
    pattern = module.params["pattern"]
    pattern_for_headers = module.params["pattern_for_headers"]

    results = {}
    # results.update({"changed": False})
    if proc_name != None:
        results.update({
            "proc_id": find_procs_by_name(proc_name)
        })
    if urllink != None and pattern != None:
        results.update({
            "test pattern": match_exp(urllink, pattern)
        })
    if urllink != None and pattern_for_headers != None:
        results.update({
            "test headers pattern": match_headers(get_site_headers(urllink), pattern_for_headers)
        })

    module.exit_json(**results)


main()
