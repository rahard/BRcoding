
# percobaan kompleksitas - big Oh
# budi rahardjo (@rahard 2021)

n=10000
import time

start_time = time.time()

a = 0
for x in range(n): 
    for y in range(n):
        a = a + 0

end_time = time.time()

elapsed = end_time - start_time
print("elapsed %s seconds ..." % elapsed)
