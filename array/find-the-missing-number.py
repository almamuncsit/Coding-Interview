# Find the number which are not common on both array

def find_missing(full_set, pertial_set):
	xor_sum = 0
	for x in full_set:
		xor_sum ^= x
		print(x, " ", xor_sum)
	for x in pertial_set:
		xor_sum ^= x
		print(x, " ", xor_sum)

	return xor_sum

a = [2, 4, 5, 3, 6, 8]
b = [2, 4, 5, 3, 12, 6, 8]
output = find_missing(a, b)

print(f"Final output {output} ")