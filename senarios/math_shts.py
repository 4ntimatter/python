import math
import time
start=time.time()

on_high_road = 10000000
not_high_road = 1
a = 0
while on_high_road>not_high_road :

    b=1/(not_high_road**2)
    a=a+b
    not_high_road +=1

print(math.sqrt(a*6))


end =time.time()
print(end-start)