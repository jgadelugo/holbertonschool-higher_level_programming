#!/usr/bin/python3
# find a peak in a list of unsorted integers

def find_peak(list_of_integers):
	if list_of_integers == None or list_of_integers == []:
		return None
	size = len(list_of_integers)
	if size == 0:
		return list_of_integers[0]
	for i in range(0, len(list_of_integers) - 1):
		if list_of_integers[i] > list_of_integers[i + 1]:
			return list_of_integers[i]
	return list_of_integers[size - 1]
