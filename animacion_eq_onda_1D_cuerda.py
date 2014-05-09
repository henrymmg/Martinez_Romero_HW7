from pylab import *
from numpy import *
from matplotlib import *
from matplotlib import animation
import sys, string, os
from StringIO import StringIO

#Codigo de la animacion creado con ayuda del repositorio:
#http://jakevdp.github.io/

#Datos iniciales
iniciales = loadtxt("datos_iniciales.txt")
x = iniciales[:,0]
u_inicial = iniciales[:,1]

#Grafica datos iniciales
plot(x,u_inicial)
title("Datos iniciales")
xlabel("X")
ylabel("U inicial")
savefig("iniciales")

#Animacion
n = 1000
figura = plt.figure()
ejes = plt.axes(xlim=(0, 100), ylim=(-1 , 1))
line, = ejes.plot([], [], lw=4, c='b')
title("Animacion de la ecuacion de onda en 1D (Cuerda vibratoria)")
xlabel("X")
ylabel("U")

data = loadtxt("datos_finales.txt");

def init():
    line.set_data([], [])
    return line,

def animate(i):
    global data
    x1 = data[:,i]
    y = data[i,:]
    line.set_data(x1, y)
    return line,


animacion = animation.FuncAnimation(figura, animate, init_func=init, frames=1000,interval=1)
plt.grid
plt.show()


