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

if((aL ==1) or (bL == 1) or (cL ==1) or (dL==1)):
    print("NÃOOOOOOOOOOOOOOOO")
while((aL1!=1) and (bL1!=1) and (cL1!=1)and (dL1!=1)):
 if (aL==2):
    for x in range(bL):
        #print(x)
        if (b1[x]==a1[1]):
            del(b1[x])
            break
        
    for x in range(cL):
        if (c1[x]==a1[1]):
            del(c1[x])
            break
        
    for x in range(dL):
        if (d1[x]==a1[1]):
            del(d1[x])
            break
    aL1 = len(a1)
    bL1 = len(b1)
    cL1 = len(c1)
    dL1 = len(d1)

    
 if (bL1==2):  
    for x in range(aL1):
        if (a1[x]==a1[1]):
            del(a1[x])
            break

    for x in range(cL1):
        if (c1[x]==a1[1]):
            del(c1[x])
            break
        
    for x in range(dL1):
        if (d1[x]==a1[1]):
            del(d1[x])
            break
    bL1 = len(b1)
    cL1 = len(c1)
    aL1 = len(a1)
    dL1 = len(d1)
    
 if (cL1==2):
    for x in range(aL1):
        if (a1[x]==c1[1]):
            del(a1[x])
            break
    for x in range(bL1):
        if (b1[x]==c1[1]):
            del(b1[x])
            break
        
    for x in range(dL1):
        if (d1[x]==c1[1]):
            del(d1[x])
            break
    aL1 = len(a1)
    bL1 = len(b1)
    dL1 = len(d1)

 if(dL1==2):
    
    for x in range(aL1):
        if (a1[x]==d1[1]):
            del(a1[x])
            break
        
    for x in range(bL1):
        if (b1[x]==d1[1]):
            del(b1[x])
            break
        
    for x in range(cL1):
        if (c1[x]==d1[1]):
            del(c1[x])
            break

#print (a ,"\n", b ,"\n", c ,"\n", d,"\n",aL,"\n", bL ,"\n", cL ,"\n", dL,"\n"  )
print ("\n",a1,"\n",b1,"\n",c1,"\n",d1)
arq.close()
