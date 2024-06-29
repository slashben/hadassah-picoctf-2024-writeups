from math import ceil, isqrt
e = 65537
x = int(input("x: "), 16)
n = int(input("n: "), 16)
c = int(input("c: "), 16)

# find p and q
p = (x + isqrt(x**2-4*n))//2
if n % p != 0:
    print("no no no!")
    exit(1)
q = n // p

phi = (p-1)*(q-1)
# find d
d = pow(e,-1,phi)


# find the message
FLAG = pow(c,d,n)
print(FLAG.to_bytes(ceil(FLAG.bit_length()/8), 'big').decode())

