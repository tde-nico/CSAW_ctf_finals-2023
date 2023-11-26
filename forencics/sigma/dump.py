from pwn import *
import numpy as np

#context.log_level = 'debug'

def sigmoid(x):
    return 1 / (1 + np.exp(x))

def inverse_sigmoid(y):
    return np.log(y / (1 - y))

def sendInp(r:remote, i):
	r.sendlineafter(b'input:', str(i).encode())


for bit in range(30):

	r = remote('172.31.88.52', 3000)

	x = [0] * 30
	x[bit] = 1

	for num in x:
		sendInp(r, num)

	r.recvline()
	r.recvline()

	value = float(r.recvline().strip().decode())

	print(value)
	print(inverse_sigmoid(value))

	r.close()

#r.interactive()
