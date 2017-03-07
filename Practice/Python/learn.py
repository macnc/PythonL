#!/usr/local/bin/python
# _*_coding: utf-8


def kw_dict(**kwarges):
	return kwarges
	
def show_args(*arges):
	return arges

print show_args(1, 2, 3)
print kw_dict(a=1, b=2)