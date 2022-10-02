# @rahard 2022
from itertools import combinations

# given a list of items ('m')
# make all possible combinations of the items

m = ['1', '3', '4', '6', '7', '9']
for i in range(len(m)):
   print("Length", i+1)
   print(list(combinations(m, i+1)))
