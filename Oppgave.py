print("oppgave 1")
a = float(input("Tall 1: "))
b = float(input("Tall 2: "))
c = float(input("Tall 3: "))
print("Snitt:", (a+b+c)/3)
print()
 
print("oppgave 2")
t = input("Tekst: ")
v = 0
for x in t:
    if x in "aeiouæøåAEIOUÆØÅ":
        v = v + 1
print("Vokaler:", v)
print()
 
 
print("oppgave 3")
s = input("Tall, komma: ")
l = s.split(",")
b = l[::-1]
print("Baklengs:", b)
print()