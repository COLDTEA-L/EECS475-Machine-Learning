import numpy;
import matplotlib.pyplot as plt;


def func(x):
    a=1/50*(x**4+x**2+10*x)
    return a


def grad_g(x):
    b=1/50*(4*x**3+2*x+10)
    return b


alpha=1;
iterations=1000;
w=numpy.zeros(iterations);
g=numpy.zeros(iterations);
ite=numpy.zeros(iterations);
w[0]=2;
g[0]=func(w[0]);

for i in range(1,iterations):
    w[i]=w[i-1]-alpha*grad_g(w[i-1]);
    print(w[i])
    g[i]=func(w[i])
    print(g[i])

for i in range(iterations):
    ite[i]=i;

plt.plot(ite,g)
plt.show()

