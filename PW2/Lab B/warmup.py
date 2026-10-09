"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1          (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
Run:  python warmup.py
"""
import numpy as np
from scipy.optimize import newton, minimize

# ---------- 2A: easy convex function ----------
def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0

# TODO 2A: minimise f three ways from x0=0 and print each result:
#   (1) gradient descent by hand (loop x = x - lr*df(x) until the step is tiny)
                                  
                                  #Formula:x_new = x_old - alpha*fprime(x)
x = 0.0
alpha = 0.1
for i in range(10000):
    x_old = x
    x_new = x_old - alpha * df(x_old)
    if abs(x_new - x_old) < 1e-8:
        x = x_new
        break
    x = x_new
print("2A Gradient Descent:", x, f(x))

#   (2) scipy.optimize.newton(df, x0, fprime=d2f)
# (2) Newton's Method

x_newton = newton(df, 0.0, fprime=d2f)
print("2A Newton:", x_newton, f(x_newton))

#   (3) scipy.optimize.minimize(f, x0, method="SLSQP")


result = minimize(f, 0.0, method="SLSQP")
print("2A SLSQP:", result.x, f(result.x))

# ---------- 2B: harder landscape ----------
def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6


# TODO 2B: run the same three methods on g, from x0=0 AND from x0=2.
#   For Newton (which solves dg(x)=0), also check the sign of d2g at the answer:
#   d2g > 0 means a minimum, d2g < 0 means a maximum.
#   In your README note: do the methods agree? did Newton find a minimum or
#   another stationary point? how did the starting point change the result?

# (1) Gradient Descent method from x0 = 0

x = 0.0
alpha = 0.01
for i in range(10000):
    x_old = x
    x_new = x_old - alpha * dg(x_old)
    if abs(x_new - x_old) < 1e-8:
        x = x_new
        break
    x = x_new
print("2B Gradient Descent from 0:", x, g(x))

# Gradient Descent from x0 = 2

x = 2.0
alpha = 0.01
for i in range(10000):
    x_old = x
    x_new = x_old - alpha * dg(x_old)
    if abs(x_new - x_old) < 1e-8:
        x = x_new
        break
    x = x_new
print("2B Gradient Descent from 2:", x, g(x))

# Newton's Method from x0 = 0

x_newton = newton(dg, 0.0, fprime=d2g)
print(
    "2B Newton from 0:",
    x_newton,
    g(x_newton),
    "second derivative:",
    d2g(x_newton)
)

# Newton's Method from x0 = 2

x_newton = newton(dg, 2.0, fprime=d2g)
print(
    "2B Newton from 2:",
    x_newton,
    g(x_newton),
    "second derivative:",
    d2g(x_newton)
)

# SLSQP from x0 = 0

result = minimize(g, 0.0, method="SLSQP")
print("2B SLSQP from 0:", result.x, g(result.x))

# SLSQP from x0 = 2

result = minimize(g, 2.0, method="SLSQP")
print("2B SLSQP from 2:", result.x, g(result.x))