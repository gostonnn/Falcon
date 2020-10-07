print("Mely síkidom kerületét és területét szeretné kiszámíttatni?")
szam=float(input("szam: "))

#py
def korkerulet(r):
    return 2*r*3.14
def korter(r):
    return r**2*3.14
def nyolcszogTerulet (a,r):
    return float (4*a*r)
def nyolcszogKerulet (a):    
    return float (8*a) 

if szam==2:
    ertek=float(input("sugar: "))
    print(korkerulet(ertek),"cm")
    print(korter(ertek),"cm2")
elif szam==4:
    a=float(input("Nyolcszög oldala [cm]: "))
    r=float(input("Nyolcszög sugara [cm]: "))
    print(nyolcszogTerulet(a,r))
    print(nyolcszogKerulet (a))
elif szam==1:
    print("passz")
else:
    print("passz")
	
#print("4 - Nyolcszög")

