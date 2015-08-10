## Testing for the Russian Peasant's Algorithm

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

def test_compute():
	assert compute(5, 10) == 50
	assert compute(6, 10) == 60
	assert compute(5, 5) == 25
	assert compute(4001, 43) == 172043
	return "All tests passed for compute() function"

print test_compute()