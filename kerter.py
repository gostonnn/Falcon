#py
def teglalapKeruletTerulet(teglalapkerulet,teglalapterulet):
	a=float(input("Adja meg a téglalap egyik oldalát"))
	b=float(input("Adja meg a téglalap másik oldalát"))
	teglalapkerulet=(a+b)*2
	teglalapterulet=a*b
	print("A teglalap kerulete",teglalapkerulet,"cm")
	print("A teglalap terulete",teglalapterulet,"cm2")
def korkerulet(r):
    return 2*r*3.14
def korter(r):
    return r**2*3.14
szam=float(input("szam: "))
print(korkerulet(szam),"cm")
print(korter(szam),"cm2")

