import collections
import json

def makehash():
    return collections.defaultdict(makehash)

myhash = makehash()

myhash['options']['title'] = 'Test Title'

print(myhash)

s = json.dumps(myhash)

print('---------')

print(s)
