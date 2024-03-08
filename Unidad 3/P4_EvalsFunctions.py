
infija = "3+5"

prefija = "+ 3 5"

postFija = " 3 5 +"

resultado = eval(infija)
#print(resultado)

from matplotlib import pyplot

x = [ i for i in range (-10,11)]
print(x)

y = [xi**2 for xi in x]
print(y)

pyplot.plot(x,y)
pyplot.show()