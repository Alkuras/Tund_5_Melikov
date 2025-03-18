# sõne="Programm"
# print(sõne)
# list_sõne=list(sõne)
# print(list_sõne)
# print(f"Viies täht: {list_sõne[4]}")
# print(f"Sõnes on {len(sõne)} t")
# elemendid=[]
# for i in range(5):                          #.append
#     elemendid.append(input(f"{i+1}. element:"))
# print(elemendid)
# for e in elemendid:
#     print(e)
# #extend
# list_sõne.extend(elemendid)
# print(list_sõne)
# print(elemendid)
# #insert
# elemendid.insert(0,"A")
# print(elemendid)
# #remove
# elemendid.remove("A")
# print(elemendid)
# #pop
# elemendid.pop(0)
# elemendid.pop()
# print(elemendid)
# #index
# ind=list_sõne.index("r")
# print(f"Täht r on {ind}-indeksiga")
# #count
# k=list_sõne.count("r")
# print(f"Täht r kohtume {k} korda sõnas {sõne}")
# #sort
# list_sõne.sort(reverse=True)
# print(list_sõne)
# #reverse
# list_sõne.reverse()
# print(list_sõne)
# #copy
# list_sõne2=list_sõne.copy()
# #clear
# list_sõne2.clear()
# print(list_sõne2)

#Töö 4.4
#1
from secrets import randbelow
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

#2
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

# #2.2

# opilased=["Juhan","Kati","Mario","Mario","Mati","Mati"]
# print(opilased)

#3

tarnid=[]
for i in range(5):                     
    tarnid.append(int(input(f"{i+1}. arv:")))
for e in tarnid:
    print("*"*e)

# #6
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



#12

# numbrid=[]
# for i in range(10):
#     numbrid.append(randbelow(100))
# print(numbrid)
# numbrid.sort()




