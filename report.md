UECM3033 Assignment #3 Report
========================================================

- Prepared by: ** Lee Hui Si **
- Tutorial Group: T3

--------------------------------------------------------

## Task 1 --  Gauss-Legendre formula

The reports, codes and supporting documents are to be uploaded to Github at: 

[https://github.com/LeeHuiSi/UECM3033_assign3](https://github.com/LeeHuiSi/UECM3033_assign3)


1. Explain how you implement your `task1.py` here.

First, the definite integral over [a,b] has to be changed to interval [-1,1] using the following formula: 

¡Ò_a^b?¡¼f(x)dx¡½=(b-a)/2 ¡Ò_(-1)^1?¡¼f((b-a)/2 x+(b+a)/2)¡½ dx

Then, approximate the definite integral over any arbitrary bounded range [a,b] by a sum of function values at specified points, x_i?{\displaystyle x_{i}}multiplied by some weights, w_i{\displaystyle w_{i}} applicable for the N=2 point rule by using the following formula:

¡Ò_a^b?¡¼f(x)dx¡½¡Ö(b-a)/2[w_1 f((b-a)/2 x_1+(b+a)/2)+w_2 f((b-a)/2 x_2+(b+a)/2)]

The answer is 0.400338097411 for n=20.


2. Explain how you get the weights and nodes used in the Gauss-Legendre quadrature.

Legendre module ¡°numpy.polynomial.legendre.leggauss(n)¡± is used to compute the sample points and weights for Gauss-Legendre quadrature.

---------------------------------------------------------

## Task 2 -- Predator-prey model

1. Explain how you implement your `task2.py` here, especially how to use `odeint`.

First, the differential equations system given is defined into a function ¡°ode_system¡± 
y_0^'=a(y_0-y_0 y_1)
y_1^'=b(-y_1+y_0 y_1)
In order to solve the system of ODEs, the module ¡°scipy.integrate.odeint¡±is used. There are few parameters that needed to defined, such as, initial values condition for part 1, y_initial = [0.1, 1.0] and t?partitioned into equally 101 points from year t=0 to t=5.


2. Put your graphs here and explain.


![ Graph of y(t) vs t, y0(0)=0.1.png](Graph of y(t) vs t, y0(0)=0.1.png)

![ Graph of y1 vs y0, y0(0)=0.1.png](Graph of y1 vs y0, y0(0)=0.1.png)


From the graphs above, the curve y0(t) is increasing but y1(t) is decreasing as the time increasing. Two of the curve intersects at a point around t=4.7. Hence, we can say that in a closed biological system, while the number of prey is increasing, the number of predator is decreasing along the time from 0 to 5 years. Lastly, around the 4.7 year, the number of prey is equal to number of predator.

Graphs for part 2 y0(0)= 0.11

![ Graph of y(t) vs t, y0(0)=0.11.png](Graph of y(t) vs t, y0(0)=0.11.png)

![ Graph of y1 vs y0, y0(0)=0.11.png](Graph of y1 vs y0, y0(0)=0.11.png)



3. Is the system of ODE sensitive to initial condition? Explain.

From the observations of graph plotted, the pattern of curve remains unchanged when different initial conditions are given. Therefore, the system of ODE can be said that it is insensitive to initial condition.
-----------------------------------

<sup>last modified: 18-Apr-2016</sup>

