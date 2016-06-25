#!/usr/local/bin/python3
# _*_coding: utf-8


import multiprocessing as mp
def foo(q):
	q.put('hello')
	
if __name__ == '__main__':
	ctx = mp.get_context('spawn')
	q = ctx.Queue()
	p = ctx.Process(target=foo, args=(q,))
	p.start()
	print(q.get())
	p.join()
