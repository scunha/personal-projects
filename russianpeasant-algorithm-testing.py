## Testing for the Russian Peasant's Algorithm
import time

CACHE = {}

def compute(num1, num2):
    key = (num1, num2)
    if key in CACHE:
        final = CACHE[key]
    else:
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
        CACHE[key] = final
    return final

def test_compute():
	assert compute(5, 10) == 50
	assert compute(6, 10) == 60
	assert compute(5, 5) == 25
	assert compute(4001, 43) == 172043
	return "All tests passed for compute() function"

print test_compute()

start_time = time.time()
timetest = compute(75000928380870987243985793843929498, 29899823498479577878238)
print "Russian Algorithm took %f seconds" % (time.time() - start_time)