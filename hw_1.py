import re
from collections import Counter
fread = input('Enter file name:\n')
try:
   fopen = open(fread)
except:
    print('.txt file cannot be opened or found')
    quit()
dic = Counter(re.findall(r"[\w']+",open(fread).read().lower()))
for k,v in sorted(dic.items()):
    print(k,v,'times')
