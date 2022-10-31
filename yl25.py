päevik = {
"eesnimi": "Robin",
"perenimi": "Pruunlep",
"sünniaasta": "2006",
"elukoht": "Kuressaare",
"lemmik magustoit": "napoleoni kook"
}

print(päevik.get("elukoht"))
print(päevik["elukoht"])

päevik.update({"lemmik magustoit": "mannavaht" })

print(päevik.keys())

print(päevik.values())

if 'isikukood' in päevik :
    print("On isikukood")
else:
    print("Pole isikukoodi")

print(len(päevik))

päevik.update({"pikkus": len(päevik)})

päevik.pop("sünniaasta")

del päevik
