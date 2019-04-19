arq = open("C:/Users/User/Videos/EP2/EP2/casamento.txt", 'r')
texto = arq.read()
r = texto[0:]
k = r.split('\n')

a = k[0]
b = k[1]
c = k[2]
d = k[3]

a1 = a.split(" ")
aL = len(a1)

b1 = b.split(" ")
bL = len(b1)

c1 = c.split(" ")
cL = len(c1)

d1 = d.split(" ")
dL = len(d1)

count  = 0


print(a1)
print(b1)
print(c1)
print(d1,"\n")
if((aL ==1) or (bL == 1) or (cL ==1) or (dL==1)):
    print("NÃOOOOOOOOOOOOOOOO")

##while((aL1!=1) and (bL1!=1) and (cL1!=1)and (dL1!=1)):
if (aL==2):
 if ('Adriano' in a1):

    if ('Adriano' in b1):
            k = b1.index('Adriano') # Posição do item que quer deletar.
            del(b1[k])
            
    if ('Adriano' in c1):
            k = c1.index('Adriano') # Posição do item que quer deletar.
            del(c1[k])

    if ('Adriano' in d1):
            k = d1.index('Adriano') # Posição do item que quer deletar.
            del(d1[k])

 if ('Bruno' in a1):

    if ('Bruno' in b1):
            k = b1.index('Bruno') # Posição do item que quer deletar.
            del(b1[k])

    if ('Bruno' in c1):
            k = c1.index('Bruno') # Posição do item que quer deletar.
            del(c1[k])

    if ('Bruno' in d1):
            k = d1.index('Bruno') # Posição do item que quer deletar.
            del(d1[k])
            
 if ('Diogo' in a1):

    if ('Diogo' in b1):
            k = b1.index('Diogo') # Posição do item que quer deletar.
            del(b1[k])

    if ('Diogo' in c1):
            k = c1.index('Diogo') # Posição do item que quer deletar.
            del(c1[k])

    if ('Diogo' in d1):
            k = d1.index('Diogo') # Posição do item que quer deletar.
            del(d1[k])

aL = len(a1)
bL = len(b1)
cL = len(c1)
dL = len(d1)
## if (bL1==2):  
##    for x in range(aL1):
##        if (a1[x]==b1[1]):
##            del(a1[x])
##            break
##
##    for x in range(cL1):
##        if (c1[x]==b1[1]):
##            del(c1[x])
##            break
##        
##    for x in range(dL1):
##        if (d1[x]==b1[1]):
##            del(d1[x])
##            break
##    bL1 = len(b1)
##    cL1 = len(c1)
##    aL1 = len(a1)
##    dL1 = len(d1)
##    
if (cL==2):
 if ('Adriano' in c1):

    if ('Adriano' in b1):
            k = b1.index('Adriano') # Posição do item que quer deletar.
            del(b1[k])
            
    if ('Adriano' in a1):
            k = a1.index('Adriano') # Posição do item que quer deletar.
            del(a1[k])

    if ('Adriano' in d1):
            k = d1.index('Adriano') # Posição do item que quer deletar.
            del(d1[k])

 if ('Bruno' in c1):

    if ('Bruno' in b1):
            k = b1.index('Bruno') # Posição do item que quer deletar.
            del(b1[k])

    if ('Bruno' in a1):
            k = c1.index('Bruno') # Posição do item que quer deletar.
            del(c1[k])

    if ('Bruno' in d1):
            k = d1.index('Bruno') # Posição do item que quer deletar.
            del(d1[k])
            
 if ('Diogo' in c1):

    if ('Diogo' in b1):
            k = b1.index('Diogo') # Posição do item que quer deletar.
            del(b1[k])

    if ('Diogo' in a1):
            k = a1.index('Diogo') # Posição do item que quer deletar.
            del(a1[k])

    if ('Diogo' in d1):
            k = d1.index('Diogo') # Posição do item que quer deletar.
            del(d1[k])
            
 if ('Leandro' in c1):

    if ('Leandro' in b1):
            k = b1.index('Leandro') # Posição do item que quer deletar.
            del(b1[k])

    if ('Leandro' in d1):
            k = d1.index('Leandro') # Posição do item que quer deletar.
            del(d1[k])

    if ('Leandro' in a1):
            k = a1.index('Leandro') # Posição do item que quer deletar.
            del(a1[k])
            
 if ('Gabriel' in d1):

    if ('Welber' in b1):
            k = b1.index('Diogo') # Posição do item que quer deletar.
            del(b1[k])

    if ('Welber' in c1):
            k = c1.index('Diogo') # Posição do item que quer deletar.
            del(c1[k])

    if ('Diogo' in a1):
            k = a1.index('Diogo') # Posição do item que quer deletar.
            del(a1[k])

 if ('Diogo' in d1):

    if ('Diogo' in b1):
            k = b1.index('Diogo') # Posição do item que quer deletar.
            del(b1[k])

    if ('Diogo' in c1):
            k = c1.index('Diogo') # Posição do item que quer deletar.
            del(c1[k])

    if ('Diogo' in a1):
            k = a1.index('Diogo') # Posição do item que quer deletar.
            del(a1[k])

aL = len(a1)
bL = len(b1)
cL = len(c1)
dL = len(d1)

if(dL==2):
    
 if ('Diogo' in d1):

    if ('Diogo' in b1):
            k = b1.index('Diogo') # Posição do item que quer deletar.
            del(b1[k])

    if ('Diogo' in c1):
            k = c1.index('Diogo') # Posição do item que quer deletar.
            del(c1[k])

    if ('Diogo' in a1):
            k = a1.index('Diogo') # Posição do item que quer deletar.
            del(a1[k])

#print (a ,"\n", b ,"\n", c ,"\n", d,"\n",aL,"\n", bL ,"\n", cL ,"\n", dL,"\n"  )
print ("\n",a1,"\n",b1,"\n",c1,"\n",d1)
arq.close()
