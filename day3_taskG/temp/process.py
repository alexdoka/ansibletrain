#! /usr/bin/env python
import psutil

def find_procs_by_name(name):
    "Return a list of processes matching 'name'."
    ls = []
    for p in psutil.process_iter(attrs=['name']):
        if p.info['name'] == name:
            ls.append(p)
    res=[]
    for i in ls:
        # print(i.info['name'])
        res.append({i.info['name']: i.pid})
    return res

pr = find_procs_by_name('bash')
# print(find_procs_by_name('java'))
print(pr)
print(1)
