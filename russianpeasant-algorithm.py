## The Russian Peasant's Algorithm
## Coded by Sarah Cunha
## 8/10/2015

#Takes the two inputted numbers and calculates them according to the algorithm
def compute(num1, num2):
    final = 0
    if (num1 % 2) != 0:
        final += num2
    while num1 != 1:
        num1 /= 2
        round(num1)
        num2 *= 2
        round(num2)
        if (num1 % 2) != 0:
            final += num2
    return final

#Infinite loop for multiple calculations    
while 1:
    int1 = raw_input("Input first integer: ")
    int2 = raw_input("Input second integer: ")
    result = compute(int(int1), int(int2))
    print result