def function(num1, num2):
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
while 1:
    int1 = raw_input("Input first integer: ")
    int2 = raw_input("Input second integer: ")
    result = function(int(int1), int(int2))
    print result