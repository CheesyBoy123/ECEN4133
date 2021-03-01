import sys


if(len(sys.argv) <= 1 and len(sys.argv[1]) > 0):
    print("Need more arguments.")
else:
    print("Converting " + sys.argv[1])
    output = ""
    for c in sys.argv[1]:
        output += "String.fromCharCode(" + str(ord(c)) +") + "
    #remove trailing + and space.
    output = output[:-2]
    print(output)
