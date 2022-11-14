import hashlib

def printed():
    
    data = "iwrupvqb"
    a = 1
    zero = 6 * '0'

    while True:
        data2 = data + str(a)
        h = hashlib.md5(data2.encode()).hexdigest()[:6]
        if h == zero:
            return a
        a += 1

print(printed())