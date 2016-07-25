#!/usr/local/bin/python
# _*_coding: utf-8

# 来自斯坦福CS231n的python课程：Python Numpy Tutorial

def quicksort(arr):
	if len(arr) <= 1:
		return arr

	privot = arr[len(arr)/2]
	left = [x for x in arr if x < privot]
	right = [x for x in arr if x > privot]
	middle = [x for x in arr if x == privot]

	return quicksort(left) + middle + quicksort(right)

i = [1, 5, 3, 4, 0, 22, 3, 12, 220]
print quicksort(i)
