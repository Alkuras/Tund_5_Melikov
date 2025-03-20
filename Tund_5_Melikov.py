# # sõne="Programm"
# # print(sõne)
# # list_sõne=list(sõne)
# # print(list_sõne)
# # print(f"Viies täht: {list_sõne[4]}")
# # print(f"Sõnes on {len(sõne)} t")
# # elemendid=[]
# # for i in range(5):                          #.append
# #     elemendid.append(input(f"{i+1}. element:"))
# # print(elemendid)
# # for e in elemendid:
# #     print(e)
# # #extend
# # list_sõne.extend(elemendid)
# # print(list_sõne)
# # print(elemendid)
# # #insert
# # elemendid.insert(0,"A")
# # print(elemendid)
# # #remove
# # elemendid.remove("A")
# # print(elemendid)
# # #pop
# # elemendid.pop(0)
# # elemendid.pop()
# # print(elemendid)
# # #index
# # ind=list_sõne.index("r")
# # print(f"Täht r on {ind}-indeksiga")
# # #count
# # k=list_sõne.count("r")
# # print(f"Täht r kohtume {k} korda sõnas {sõne}")
# # #sort
# # list_sõne.sort(reverse=True)
# # print(list_sõne)
# # #reverse
# # list_sõne.reverse()
# # print(list_sõne)
# # #copy
# # list_sõne2=list_sõne.copy()
# # #clear
# # list_sõne2.clear()
# # print(list_sõne2)

# # #Töö 4.4
# # #1
from random import *
from string import *

vokaali=["a","e","y","u","i","o","ö","ü","ä","õ"]
numbrid=digits
märgid=punctuation
konsonanti="qwrtpsdfghjklzxcvbnm"
v=k=n=m=t=0
tekst=input("Sisend (sõna või lause):").lower()
tekst_list=list(tekst)
print(tekst_list)
if " " in tekst_list:
    print("See on lause")

    for s in tekst_list:
        if s in vokaali:
            v+=1
        elif s in konsonanti:
            k+=1
        elif s in numbrid:
            n+=1
        elif s in märgid:
            m+=1
        elif s==" ":
            t+=1
    print(f"V: {v}\nK: {k}\nN: {n}\nM: {m}\nT: {t}")

else:
    print(f"Kokku on {len(tekst_list)}")
    for s in tekst_list:
        if s in vokaali:
            v+=1
        elif s in konsonanti:
            k+=1
    print(f"V: {v}\nK: {k}")

# #2
#2.1
p=0
nimed=[]
print("Sisesta nimed:")
for i in range(5): 
   nimed.append(input(f"{i+1}. nimi: "))

print(f"Viimati lisatud nimi: {nimed[4]}")
nimed.sort()
for e in nimed:
    p+=1
    print(f"{p}. {e} ")
print(nimed)
print("Kas soovite mingi nimi asendada?")
a =int(input("Sisesta nimi numbri: "))
asend =input("Sisesta nimi ise: ")
nimed.remove(nimed[a-1])
nimed.insert(a-1,asend)
nimed.sort()
print(nimed)

# # # #2.2

opilased=["Juhan","Kati","Mario","Mario","Mati","Mati"]
opilased2=opilased.copy()
print(opilased)
if opilased.count("Mario")>1:
    opilased2.remove("Mario")
if opilased.count("Mati")>1:
    opilased2.remove("Mati")
print(opilased2)

# #2.1

# vanus=[2,5,63,85,33,12,22,55,77,42,12,42,16,]
# vanus.sort

# #3

tarnid=[]
for i in range(5):                     
    tarnid.append(int(input(f"{i+1}. arv:")))
for e in tarnid:
    print("*"*e)

4
try:
    index=input("Sisesta oma post indeksi: ")
    index_list=list(index)
    if len(index)==5:
        if index.isdigit()==True:
            if index_list[0]=="1":
                print("See index kulub Tallinna")
            elif index_list[0]=="2":
                print("See index kulub Narva,Narva-Jõesuu")
            elif index_list[0]=="3":
                print("See index kulub Kohtla-Järve")
            elif index_list[0]=="4":
                print("See index kulub Ida-Virumaa, Lääne-Virumaa, Jõgevamaa")
            elif index_list[0]=="5":
                print("See index kulub Tartu linn")
            elif index_list[0]=="6":
                print("See index kulub Tartumaa, Põlvamaa, Võrumaa, Valgamaa")
            elif index_list[0]=="7":
                print("See index kulub Viljandimaa, Järvamaa, Harjumaa, Raplamaa")
            elif index_list[0]=="8":
                print("See index kulub Pärnumaa")
            elif index_list[0]=="9":
                print("See index kulub Läänemaa, Hiiumaa, Saaremaa")
            
        else:
            print("Sisesta numbrid!!!")
        if index_list[0]=="1" or index_list[0]=="2" or index_list[0]=="3":
            print("Jääge kodus!")
        else:
            print("Kange maski")
    else:
        print("Indeksis on viis numbri")

except Exception as e:
         print ("Viga:",e)


# # #6
numbrid=[1,2,3,4,5,6,7,8,9,2224,55342,624642,1134,5134,6246,1341,75475,32413,425,11,64,747,341,543,143,68,488,324,644,]
numbrid.sort(reverse=True)
print(numbrid)
print()
a=numbrid[0]/len(numbrid)
numbrid.remove(numbrid[0])
numbrid.insert(0,a)
print(numbrid)


#7

numbrid=[1,2,3,4,5,6,7,8,9,2224,55342,624642,1134,5134,6246,1341,75475,32413,425,11,64,747,341,543,143,68,488,324,644,]
numbrid.sort(reverse=True)
print(numbrid)
numbrid.sort()
print(numbrid)

# #9
while True:
    try:
        nimi=input("Sisesta oma nimi: ")
        if nimi.isalpha()==True:
            break

    except:
        print("Kasuta ainult tähed")
cap=nimi.capitalize()
print(f"Tere, {cap}!")
nimi_list=list(nimi)
vokaali=["a","e","y","u","i","o","ö","ü","ä","õ"]
konsonanti="qwrtpsdfghjklzxcvbnm"
v=k=0  
for s in nimi_list:
        if s in vokaali:
            v+=1
        elif s in konsonanti:
            k+=1
print(f"V: {v}\nK: {k} \nLen:{len(nimi)}")
nimi_list.sort()
for i in nimi_list:
    print(i)

#11
alph=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
soov=int(input("Palju tahad näha?"))
i=0
while i <soov:
    i+=1
    print(alph[i-1]*i)



#12

numbrid=[]
for i in range(10):
    numbrid.append(randint(1,100))
numbrid.sort(reverse=True)
print(numbrid)
maks=numbrid[0]
minn=numbrid[9]
numbrid.remove(numbrid[0])
numbrid.remove(numbrid[8])
numbrid.append(maks)
numbrid.insert(0,minn)
print(numbrid)


# #13

