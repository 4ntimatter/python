num = 101

a = 2
while a < num:
    if (num % a ==0):
        print("not prim")
    elif a==num-1 and num % a!=0 :
        print("isnt prim")
        break

    else:
      a += 1
