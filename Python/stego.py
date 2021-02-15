# create steganography
# stuff names into a 80x24 grid
# 2021 @rahard (budi rahardjo)

firstname = "BUDI"
lastname = "RAHARDJO"
width = 80
height = 24


# let the fun begins #
######################
len1 = len(firstname)
len2 = len(lastname)

# where to put
# the rows - going to exclude the 1st row. to obvious
import random
row1 = random.randint(1,height)
row2 = random.randint(1,height)
# make sure first name first
if (row1 > row2):
   row1, row2 = row2, row1

# the columns
col1 = random.randint(0, width - len1)
col2 = random.randint(0, width - len2)

# the resulting position
#print(col1,row1)
#print(col2,row2)

# now populate 80x24 with random "A" - "Z"
import string
screen=[]
for row in range(height):
   x =''.join(random.choice(string.ascii_uppercase) for x in range(80))
   screen.append(x)

# now replace strings with names
# firstname
x=screen[row1]
#print(x)
for i in range(len1):
   position = i+col1
   x = x[:position] + firstname[i] + x[position+1:]
#print(x)
screen[row1]=x

# lastname
x=screen[row2]
#print(x)
for i in range(len2):
   position = i+col2
   x = x[:position] + lastname[i] + x[position+1:]
#print(x)
screen[row2]=x

# and ... here's a song for you ...
for y in (screen):
   print(y)
