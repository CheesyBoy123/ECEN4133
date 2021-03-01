import hashlib

b = 10000000000
a = 10000000

for i in range(a, b):
    byte_number = str(i).encode()
    hashed_number = hashlib.md5(byte_number).digest()
    if(hashed_number.startswith(b'\'||1#')):
        print(i)
        print(hashed_number)
print("Finished.")
