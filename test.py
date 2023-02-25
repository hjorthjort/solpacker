import binpacking

b = { 'a': 10, 'b': 10, 'c':11, 'd':1, 'e': 2,'f':7, 'g': 9, 'h': 10, 'i': 5, 'j': 7, 'k': 8 , 'l': 2, 'm': 3, 'n': 4, 'o': 6, 'p': 7, 'q': 2, 'r': 3, 's': 4, 't': 6, 'u': 7, 'v': 2, 'w': 3, 'x': 4, 'y': 6, 'z': 7 }
print(binpacking.pack(b, 11, 14))
sys.exit(0)