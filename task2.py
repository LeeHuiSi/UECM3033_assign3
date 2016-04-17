import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# generate the given ODE system into this function
def ode_system(y, t, a, b):
    y0, y1 = y
    dydt = [a*(y0-y0*y1), b*(-y1+y0*y1)]
    return dydt
# given parameters   
a = 1.0
b = 0.2
# part1 given y0(0)=0.1
y_initial = [0.1, 1.0]
t = np.linspace(0,5,101)
sol = odeint(ode_system,y_initial,t,args=(a, b))

# graph of y0 and y1 against t
plt.plot(t, sol[:, 0], 'b', label='y0(t)')
plt.plot(t, sol[:, 1], 'g', label='y1(t)')
plt.title('Graph of y(t) against t, y0(0)=0.1')
plt.legend(loc='best')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid()
plt.show()


# plotting the graph for y1 against y0
plt.plot(sol[:, 0],sol[:,1], 'b')
plt.title('Graph of y1 against y0, y0(0)=0.1')
plt.xlabel('y0')
plt.ylabel('y1')
plt.grid()
plt.show()

# part2 given y0(0)=0.11
y_initial = [0.11, 1.0]
sol2 = odeint(ode_system,y_initial,t,args=(a, b))

#Graph of y0 and y1 against t
plt.plot(t, sol2[:, 0], 'b', label='y0(t)')
plt.plot(t, sol2[:, 1], 'r', label='y1(t)')
plt.title('Graph of y(t) against t, y0(0)=0.11')
plt.legend(loc='best')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid()
plt.show()


# plotting the graph for y1 against y0
plt.plot(sol2[:, 0],sol2[:,1], 'r')
plt.title('Graph of y1 against y0, y0(0) = 0.11')
plt.xlabel('y0')
plt.ylabel('y1')
plt.grid()
plt.show()