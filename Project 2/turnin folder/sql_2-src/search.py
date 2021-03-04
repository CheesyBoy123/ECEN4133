import hashlib

b = 1000000000000000000000000


for i in range(0, b):
    byte_number = str(i).encode()
    hashed_number = hashlib.md5(byte_number).digest()
    if(b'\'||1#' in hashed_number):
        print(i)
        print(hashed_number)
        break
print("Finished.")
