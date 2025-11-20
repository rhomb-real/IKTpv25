#List-loend
l=[]
print(f"Listi algseis: {l}")
while True:
    print("Tee valik:\n1- Lisa elemente\n2-Lisa elemte pos-le\n3-Emalda elemente pos järgi")
    print("4-Eemalda element nime järgi\n5-Lisa põhiloendisse uus loend\n6-Sorteerib listi")
    print("7-List vastupidine järjekord\n8-Täiesti selge listi")
    while True:
        try:
            valik=int(input())
            break
        except:
            print("Arvud: 1-. . .-n")
    print("Töö listiga")
    if valik==1:
        while True:
            try:
                i=int(input("Mitu elementi soobid lisada? "))
                if i>0:

                    break
                else:
                    print("Arvud >0")
            except:
                print("Täisarvud on vaja kasutada")
        for element_id in range(i):
            element=input(f"{element_id}. element:")
            l.append(element)
        
    elif valik==2:
        while True:
            try:
                pos=int(input(f"Positsioon kuhu soobid lisada (0-{len(l)})"))
                if 0<=pos<=len(l):
                    break
                else:
                    print(f"Positsioon peab olema vahemikus 0 kuni {len(l)}")
            except:
                print("Täisarv on vaja kasutada")
        element=input("Sisesta element mida soovid lisada:")
        l.insert(pos, element)
    elif valik==3:
        while True:
            try:
                pos=int(input(f"Positsioon kust soovid emaldada (0-{len(l)-1}): "))
                if 0<=pos<=len(l)-1:
                    break
                else:
                    print(f"Positsioon peab olema vahemikus 0 kuni {len(l)-1}")
            except:
                print("Täisarv on vaja kasutada")
        eem_element=l.pop(pos)
        print(f"Eemaldatud element on {eem_element}")
    elif valik==4:
        element=input("Sisesta element mida soobid eemaldada:")
        mitu=l.count(element)
        if mitu==0:
            print("Elementi ei leitud")
        else:
            for e in range(mitu):
                print(f"Eemaldatud element '{element}' {mitu} positsioonilt")
                l.remove(element)
        print(f"Eemaldati {mitu} elementi")
    elif valik==5:
        n=[]
        while True:
            try:
                i=int(input("Mitu elementi? "))
                if i>0:

                    break
                else:
                    print("Arvud >0")
            except:
                print("Täisarvud on vaja kasutada")
        for element_id in range(i):
            element=input(f"{element_id}. n element:")
            n.append(element)
        l.extend(n)
    elif valik==6:
        l.sort()
    elif valik==7:
        l.reverse()
    elif valik==8:
        l.clear()    
    else:
        print("Vale number!")
    print(f"Uuendatud list on {l}")