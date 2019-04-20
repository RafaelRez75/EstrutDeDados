arq = open("C:/Users/User/Videos/EP2/EP2/casamento.txt", 'r')
texto = arq.read()
k = [6]
l = [6]
m = [6]
r = texto[0:]
e = r.split('\n')

a = e[0]
b = e[1]
c = e[2]
d = e[3]

a1 = a.split(" ")
aL = len(a1)

b1 = b.split(" ")
bL = len(b1)

c1 = c.split(" ")
cL = len(c1)

d1 = d.split(" ")
dL = len(d1)

count  = 0

r = aL + bL + cL + dL
print(r)

#if((aL[1]!= " ")and(bL[1]!= " ")and(cL[1]!= " ")and(dL[1]!= " ")):
for x in range(aL):
    if(x==0):
        x = 1
    for x1 in range(bL):
        if(x1==0):
            x1 = 1
        for x2 in range(cL):
            if(x2==0):
                x2 = 1
            for x3 in range(dL):
                if(x3==0):
                    x3 = 1
            p = a1[0] + a1[x] + b1[0] + b1[x1] + c1[0] + c1[x2] + d1[0] + d1[x3]
            print(p)
