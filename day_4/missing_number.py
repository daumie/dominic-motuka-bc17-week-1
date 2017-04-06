def find_missing(array_1,array_2):
	#convert the arrays to sets
	array_1_set = set(array_1)
	array_2_set = set(array_2)

	extra_number_set = set(array_1) ^ set(array_2)

	#convert set to array
	missing_array = list(extra_number_set)

	return missing_array
print(find_missing([2],[2]))