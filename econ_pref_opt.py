print("cell 1")
import matplotlib.pyplot as plt
import numpy as np
def max_oil(p_1, p_2, e_1, e_2):
    return (p_1*e_1+p_2*e_2)/p_1

def max_gas(p_1, p_2, e_1, e_2):
    return (p_1*e_1+p_2*e_2)/p_2

y_0=max_oil(5,5,25,10) #maximal holdings for oil
x_0=max_gas(5,5,25,10) #maximal holdings for gas

x_1=max_gas(5,10,25,5) #price of gas rise
y_1=max_oil(10,10,12.5,5) #price of oil rise

x=np.linspace(0, x_0)
y=y_0-x

x_i=np.linspace(0, x_1)
y_i=y_0-2*x_i

x_j=np.linspace(0, x_1)
y_j=y_1-x_i

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Budget Constraint 1')
plt.plot(x_i, y_i, label='Budget Constraint 2')
plt.plot(x_j, y_j, label='Budget Constraint 3')
plt.axvline(x=0, color='black',linewidth=0.5)
plt.axhline(y=0, color='black',linewidth=0.5)
plt.xlabel('Gas (Per Unit)')
plt.ylabel('Crude Oil (Per Unit)')
plt.title('Budget Constraints for Murphy')
plt.legend()
plt.grid(True)
plt.show()

print("cell 2")
import matplotlib.pyplot as plt
import numpy as np
def budget_constraint(p1, p2, p3, e1, e2, e3):
    W = p1 * e1 + p2 * e2 + p3 * e3
    x1_values = np.linspace(0, W/p1, 100)
    x2_values = np.linspace(0, W/p2, 100)
    X1, X2 = np.meshgrid(x1_values, x2_values)
    X3 = (W - p1 * X1 - p2 * X2) / p3
    X3_new = (np.abs(X3) + X3) / 2
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X1, X2, X3_new, cmap='viridis')
    ax.set_xlabel('Crude Oil (x1)')
    ax.set_ylabel('Gas (x2)')
    ax.set_zlabel('Coal (x3)')
    ax.set_title('Budget Constraint')
    plt.show()

p1, p2, p3, e1, e2, e3 = 5, 5, 10, 25, 10, 15
budget_constraint(p1, p2, p3, e1, e2, e3)

print("cell 3")
import matplotlib.pyplot as plt
import numpy as np
def plot_budget_constraint(p1, p2, m):
    x1_values = np.linspace(0, m/p1, 100)
    x2_values = (m - p1 * x1_values) / p2
    plt.plot(x1_values, x2_values, label='Budget Constraint')
    plt.xlabel('Good 1')
    plt.ylabel('Good 2')
    plt.title('Budget Constraint')
    plt.grid(True)
    plt.legend()
    plt.show()

p1, p2, m = 5, 5, 20
plot_budget_constraint(p1, p2, m)

print("cell 4")
from scipy.optimize import fmin_cobyla

def utility(x):
    return -1 * (np.log(x[0]) + np.log(x[1]))

def constraint1(x, p1, p2, m):
    return m - p1*x[0] - p2*x[1]

def plot_optimal_choice_and_indifference_curve(p1, p2, m):
    x0 = [1, 1]  # Initial guess
    x_opt = fmin_cobyla(utility, x0, [lambda x: constraint1(x, p1, p2, m)])
    optimal_utility = -utility(x_opt)

    x1_values = np.linspace(0.1, m/p1, 100)
    x2_values = (m - p1 * x1_values) / p2
    plt.plot(x1_values, x2_values, label='Budget Constraint')

    print(x_opt)
    plt.scatter(x_opt[0], x_opt[1], color='red', label='Optimal Choice')

    x2_indifference = np.exp(optimal_utility - np.log(x1_values))
    plt.plot(x1_values, x2_indifference, '--', label='Indifference Curve')
    plt.xlabel('Good 1')
    plt.ylabel('Good 2')
    plt.title('Optimal Choice and Indifference Curve')
    plt.grid(True)
    plt.legend()
    plt.show()

p1, p2, m = 1, 5, 20
plot_optimal_choice_and_indifference_curve(p1, p2, m)

print("cell 5")
def utility(x):
    return -1 * (np.log(x[0]) + np.log(x[1]))

def constraint_budget(x, p1, p2, m):
    return m - p1*x[0] - p2*x[1]

def optimal_choice_for_p1(p1_values, p2, m):
    x1_choices = []
    x2_choices = []
    for p1 in p1_values:
        x0 = [1, 1]
        x_opt = fmin_cobyla(utility, x0, [lambda x: constraint_budget(x, p1, p2, m)])
        x1_choices.append(x_opt[0])
        x2_choices.append(x_opt[1])
    return x1_choices, x2_choices

p1_values = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
p2, m = 5, 20
x1_choices, x2_choices = optimal_choice_for_p1(p1_values, p2, m)

fig, ax = plt.subplots(2, 1, figsize=(8, 10))

# Numerical solutions
ax[0].plot(p1_values, x1_choices, label='x1(p1)', color='blue')
ax[0].plot(p1_values, x2_choices, label='x2(p1)', color='red')
ax[0].set_title('Optimal Choices as a Function of p1 (Numerical)')
ax[0].set_xlabel('p1')
ax[0].set_ylabel('Quantity')
ax[0].legend()

p11_values = np.linspace(1, 9)
closed_form_x1=10/p11_values
closed_form_x2=2/p11_values*p11_values
ax[1].plot(p11_values, closed_form_x1, label='x1(p1)', color='blue')
ax[1].plot(p11_values, closed_form_x2, label='x2(p1)', color='red')
ax[1].set_title('Optimal Choices as a Function of p1 (Closed Form)')
ax[1].set_xlabel('p1')
ax[1].set_ylabel('Quantity')
ax[1].legend()

plt.tight_layout()
plt.show()

print("cell 6")

def utility(x):
    return -1 * (np.log(x[0]) + np.log(x[1]))

def constraint_budget(x, p1, p2, m):
    return m - p1*x[0] - p2*x[1]
def optimal_choice_for_m(m_values, p1, p2):
    x1_choices = []
    x2_choices = []
    for m in m_values:
        x0 = [1, 1]
        x_opt = fmin_cobyla(utility, x0, [lambda x: constraint_budget(x, p1, p2, m)])
        x1_choices.append(x_opt[0])
        x2_choices.append(x_opt[1])
    return x1_choices, x2_choices

m_values = np.array([20, 25, 30, 35, 40, 45, 50])
p1, p2 = 5, 5
x1_choices_m, x2_choices_m = optimal_choice_for_m(m_values, p1, p2)

fig, ax = plt.subplots(2, 1, figsize=(8, 10))

# Numerical solutions
ax[0].plot(m_values, x1_choices_m, label='x1(m)', color='blue')
ax[0].plot(m_values, x2_choices_m, label='x2(m)', color='red')
ax[0].set_title('Optimal Choices as a Function of m (Numerical)')
ax[0].set_xlabel('m')
ax[0].set_ylabel('Quantity')
ax[0].legend()

mm_values = np.linspace(20, 50)
closed_form_x1_m=mm_values/10
closed_form_x2_m=mm_values/10
ax[1].plot(mm_values, closed_form_x1_m, label='x1(m)', color='blue')
ax[1].plot(mm_values, closed_form_x2_m, label='x2(m)', color='red')
ax[1].set_title('Optimal Choices as a Function of m (Closed Form)')
ax[1].set_xlabel('m')
ax[1].set_ylabel('Quantity')
ax[1].legend()

plt.tight_layout()
plt.show()

print("cell 7")
def utility_asymmetric(x, theta1, theta2):
    return -1 * ((x[0]**(1-theta1))/(1-theta1) + (x[1]**(1-theta2))/(1-theta2))  # Negative because we want to maximize

def optimal_choice_for_p1_asymmetric(p1_values, p2, m, theta1, theta2):
    x1_choices = []
    x2_choices = []
    for p1 in p1_values:
        x0 = [1, 1]  # Initial guess
        x_opt = fmin_cobyla(lambda x: utility_asymmetric(x, theta1, theta2), x0, [lambda x: constraint_budget(x, p1, p2, m)])
        x1_choices.append(x_opt[0])
        x2_choices.append(x_opt[1])
    return x1_choices, x2_choices

def optimal_choice_for_m_asymmetric(m_values, p1, p2, theta1, theta2):
    x1_choices = []
    x2_choices = []
    for m in m_values:
        x0 = [1, 1]
        x_opt = fmin_cobyla(lambda x: utility_asymmetric(x, theta1, theta2), x0, [lambda x: constraint_budget(x, p1, p2, m)])
        x1_choices.append(x_opt[0])
        x2_choices.append(x_opt[1])
    return x1_choices, x2_choices


theta1, theta2 = 4, 2

# Optimal choice for p1
x1_choices_asymmetric, x2_choices_asymmetric = optimal_choice_for_p1_asymmetric(p1_values, p2, m, theta1, theta2)

# Optimal choice for m
x1_choices_m_asymmetric, x2_choices_m_asymmetric = optimal_choice_for_m_asymmetric(m_values, p1, p2, theta1, theta2)

fig, ax = plt.subplots(2, 1, figsize=(8, 10))

# Numerical solutions for p1
ax[0].plot(p1_values, x1_choices_asymmetric, label='x1(p1)', color='blue')
ax[0].plot(p1_values, x2_choices_asymmetric, label='x2(p1)', color='red')
ax[0].set_title('Optimal Choices as a Function of p1 with Asymmetric Utility')
ax[0].set_xlabel('p1')
ax[0].set_ylabel('Quantity')
ax[0].legend()

# Numerical solutions for m
ax[1].plot(m_values, x1_choices_m_asymmetric, label='x1(m)', color='blue')
ax[1].plot(m_values, x2_choices_m_asymmetric, label='x2(m)', color='red')
ax[1].set_title('Optimal Choices as a Function of m with Asymmetric Utility')
ax[1].set_xlabel('m')
ax[1].set_ylabel('Quantity')
ax[1].legend()

plt.tight_layout()
plt.show()