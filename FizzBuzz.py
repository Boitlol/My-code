num=0
r=int(input("what is the range\n"))
for i in range(r):
    num=i
    if num%5==0 and num%3==0:
        print("fizzbuzz")
    elif num%3==0:
        print("fizz")
    elif num%5==0:
        print("buzz")
    else:
        print(num)