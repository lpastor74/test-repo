import math
import sys
from os import rename

import requests

# print(sys.executable)
print(sys.version)
print('Hello')
test = 'Test'
r = requests.get('https://github.com/timeline.json')
print(r.status_code)
print(requests.codes.teapot)
print(r.text)

print("END")
