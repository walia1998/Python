# Two types of Modules in Python 
#  - Build in Modules
#  - External Modules

import math
import mymodule
import requests


mymodule.hello()

print(math.sqrt(16))

r = requests.get('https://www.google.com')
print(r.text)
