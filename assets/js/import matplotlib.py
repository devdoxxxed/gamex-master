import matplotlib.pyplot as plt

def f(x, y):
    return y - y**2

def improved_euler_method(x0, y0, h, N):
    results = [(x0, y0)]
    for i in range(N):
        y_star = results[-1][1] + h * f(results[-1][0], results[-1][1])
        y_next = results[-1][1] + (h/2) * (f(results[-1][0], results[-1][1]) + f(results[-1][0] + h, y_star))
        x_next = results[-1][0] + h
        results.append((x_next, y_next))
    return results

# (a) Solve the problem for h=0.1 and h=0.2 with 2 steps each
result_h_0_1 = improved_euler_method(0, 0.2, 0.1, 2)
result_h_0_2 = improved_euler_method(0, 0.2, 0.2, 2)

print("Solution for h=0.1:", result_h_0_1)
print("Solution for h=0.2:", result_h_0_2)

# (d) Graph solution curves
h_values = [0.1, 0.2]
N_values = [2, 5, 10]  # You can adjust the number of steps as needed

for h in h_values:
    for N in N_values:
        result = improved_euler_method(0, 0.2, h, N)
        x_values = [x for x, y in result]
        y_values = [y for x, y in result]

        plt.plot(x_values, y_values, label=f'h={h}, N={N}')

plt.title('Improved Euler\'s Method for Logistic Population Model')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()