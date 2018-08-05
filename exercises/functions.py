
def is_prime(x):
	for i in range(1,x-1):
		if x%i==0:
			return False
	return True

print(is_prime(5191))
