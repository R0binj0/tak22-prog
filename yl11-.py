a = input("Sisesta midagi: ").strip()

if len(a)>= 7:
    if (len(a) % 2) == 0:
        print("sobib")
    else:
        print("ei sobi")
