#VA = float(input("Ingrese la variacion de la velociad : "))
#AT = float(input("Ingrese tiempo de variacion : "))
#VF = float(input("ingrese la velocidad final : "))
#var = (VA - AT)/ VF
#print("la acelaracion inicial es de : " , var)
m = 0
s = 0
v = []
D = int(input("Digite la distancia a recorrer : "))
while D > m:
    m = int(input("Digite distancia recorrida : "))
    s = int(input("Digite el tiempo acumulado : "))
    v.append({m,s})
    print("velocidad : ", m/s)
a = D * s / m
print(a)
m = 0
r = s
for i in v:
    m = (m + list(i)[0]) / 2
    s = (s + list(i)[1]) /2
    if s > r:
        r = s    
    print(m / (s * r))
print(D / (s * r))   
