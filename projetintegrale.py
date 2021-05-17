#coding: utf-8
import math

""" Projet integrale Driss NAIT BELKACEM"""


def rectangle_gauche(fx,a,b,n):
    var1 = float((b - a))/n
    res = 0
    for i in range(n):
        res += var1*fonction(fx,(a+i*var1))#var1 * f(a(k))
    return res

def rectangle_droit(fx,a,b,n):
    var1 = float((b - a))/n
    res = 0
    for i in range(1,n+1):
        res += var1*fonction(fx,(a+i*var1))
    return res

def rectangle_medians(fx,a,b,n):
    var1 = float((b - a))/n
    res = 0
    for i in range(n):
        res+= var1*fonction(fx,(((a+i*var1)+(a+(i+1)*var1))/2))
    return res
"""
def trapezes(fx,a,b,n):
    var1 = float((b - a))/(2*n)
    h = float((b - a))/n
    res = 0
    for i in range(1,n):
        res += var1*(fonction(fx,a)+fonction(fx,b)+2*fonction(fx,a+i*h))
    return res
"""
def trapezes(fx,a,b,n):
    var1 = float((b - a))/(2*n)
    h = float((b - a))/n
    var2 = 0
    for i in range(1,n):
        var2 += fonction(fx,a+i*h)#f(a(k))
    res = var1*(fonction(fx,a)+fonction(fx,b)+2*var2)
    return res

"""
def trapezes(fx,a,b,n):
    var1 = float((b - a))/(n)
    res =  0.5*(fonction(fx,a)+fonction(fx,b))
    for i in range(1,n):
        res += fonction(fx,a+i*var1)
    res *= var1
    return res
"""
def simpson(fx,a,b,n):
    var1 = float((b-a))/(6*n)  #f(a(k))
    h = float((b - a))/n
    h2 = float((b - a))/(2*n)
    res = (fonction(fx,a)+fonction(fx,b))
    res1 = 0
    res2 = 0
    for i in range(1,n):
        res1 += fonction(fx,a+i*h)
    res1 = 2*res1
    for i in range(0,n):
        res2 += fonction(fx,a+(2*i+1)*h2)
    res2 = 4 * res2
    resf = var1*(res + res1 + res2)
    return res, res1, res2, resf


#le script qui donnera la valeur de la robabilité P(X<t) pour t >= 0 lorsque X suit une loi nomale de paramétres m et sig >0 fourni par l'utilisateur
def valeurProbabilite(a, b, m, n):
	sig = raw_input("entrez la valeur de sigma : ")
	sig = float(sig)	
	#print(type(sig))
	var1 = float((b - a))/n
  	res = 0
 	for i in range(n):
   	  res += var1*((a+i*var1)*float(sig)+ m) #f(a(k))*sig + m // la fonction sous la loi normale sig * x + m 
	return res

def valeurProbabilite2(a, b, m, n):
	sig = raw_input("entrez la valeur de sigma : ")
	sig = float(sig)
	a = float(m - sig)
	b = float(m + sig)
	#print(type(sig))
	var1 = float((b - a))/n
  	res = 0
 	for i in range(n):
   	  res += var1*((a+i*var1)*float(sig)+ m) #f(a(k))*sig + m // la fonction sous la loi normale sig * x + m 
	return res

def fonction(fx,x):
    if (fx=="x^2"):
        return x*x
    elif (fx=="x^3"):
        return x*x*x
    elif (fx=="sin(x)"):
        return math.sin(x)
    elif (fx=="ln(x)"):
        return math.log(x)
    elif (fx=="cos(x)"):
        return math.cos(x)
    elif (fx=="e^-x"):
        return math.e**(-x)
    elif (fx=="e^-x^2"):
        return math.e**(-x**2)
    elif (fx=="1/(1+x^2)"):
        return 1/(1+x**2)





""
# EXERCICE 1 #
fx = "x^2"
res = rectangle_gauche(fx,0,1,10)
print "Ex1 :",res
# EXERCICE 2 #
res2 = rectangle_droit(fx,0,1,10)
print "Ex2 : ",res2
# EXERCICE 3 #
res3 = rectangle_medians(fx,0,1,10)
print "Ex3 : ",res3

# EXERCICE 4 #
fx1 = "x^3"
res4 = rectangle_medians(fx1,0,1,10)
print "Ex 4.1 : ",res4
fx2 = "sin(x)"
res5 = rectangle_medians(fx2,-math.pi/2,math.pi/2,10) #f(x), -pi/2, pi/2, 10
print "Ex 4.2 : ",res5
fx3 = "ln(x)"
res6 = rectangle_medians(fx3,1,math.e,10)#f(x), 1, ecponentiel, 1°	
print "Ex 4.3 : ",res6

# EXERCICE 5 #
fx4 = "x^3"
res7 = trapezes(fx4,0,1,10)
print "Ex 5.1.a : ",res7
fx5 = "cos(x)"
res8 = trapezes(fx5,0,math.pi/2,10)
print "Ex 5.2.b : ",res8
fx6 = "e^-x"
res9 = trapezes(fx6,0,50,10)
print "Ex 5.3.c avec n = 10 : ",res9
res10 = trapezes(fx6,0,50,1000)
print "Ex 5.3.c avec n = 1000 : ",res10

# EXERCICE 6 #
fx7 = "x^2"
res11 = simpson(fx7,0,1,3)
print "Ex 6.1 : ",res11
fx8 = "e^-x^2"
res12 = simpson(fx8,-3,3,10)
print "Ex 6.2.a : ",res12
fx9 = "1/(1+x^2)"
res13 = simpson(fx9,-3,3,10)
print "Ex 6.2.b : ",res13


#EXERCICE 7
res14 = valeurProbabilite(0, 1, 0, 3)
print "Ex 7.1 ", res14
res15 = valeurProbabilite2(0,1,0,3)
print "Ex7.2", res15
