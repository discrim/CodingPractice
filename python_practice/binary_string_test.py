aa = 'a string'
print("type(aa): ", type(aa))
print("aa: ", aa)
print("type(aa.encode()): ", type(aa.encode()))
print("aa.encode(): ", aa.encode())

bb = b'\x41'
bb = b'u\x01'
print("type(bb): ", type(bb))
print("bb: ", bb)
print("type(bb.decode()): ", type(bb.decode()))
print("bb.decode(): ", bb.decode())