#! /usr/bin/python
# count the number of characters from STDIN
# budi rahardjo

import sys
from collections import Counter
import re

regex = re.compile('[^a-zA-Z]')
karakter = list()
for line in sys.stdin:
    line = regex.sub('',line)
    karakter.extend(list(line.lower()))
#print karakter
print Counter(karakter)
