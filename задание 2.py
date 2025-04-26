import matplotlib.pyplot as plt
import numpy as np

num_original_points = 5
num_shifted_points = 10
original_points_x = np.random.rand(num_original_points) * 17
original_points_y = np.random.rand(num_original_points) * 12

shifted_x_data = []
shifted_y_data = []
central_x_means = []
central_y_means = []
x_errors = []
y_errors = []

for i in range(num_original_points):
    x_deviations = np.random.normal(0, 0.9, num_shifted_points)
    y_deviations = np.random.normal(0, 0.7, num_shifted_points)
    x_shifted = original_points_x[i] + x_deviations
    y_shifted = original_points_y[i] + y_deviations

    shifted_x_data.append(x_shifted)
    shifted_y_data.append(y_shifted)

    x_mean = np.mean(x_shifted)
    y_mean = np.mean(y_shifted)
    x_error = np.std(x_shifted)  
    y_error = np.std(y_shifted)  

    central_x_means.append(x_mean)
    central_y_means.append(y_mean)
    x_errors.append(x_error)
    y_errors.append(y_error)

plt.figure(figsize=(10, 10))

colors = ['blue', 'green', 'red', 'purple', 'orange']
markers = ['o', 's', '^', 'v', 'D']

for i in range(num_original_points):
    plt.scatter(shifted_x_data[i], shifted_y_data[i],
                c=colors[i], marker=markers[i], label=f'Смещенные точки {i+1}', alpha=0.5)

plt.errorbar(central_x_means, central_y_means, xerr=x_errors, yerr=y_errors,
             fmt='*', color='black', label='Центральные точки с погрешностями', markersize=10)

plt.scatter(original_points_x, original_points_y,
            marker='x', s=100, color='black', label='Исходные точки')

plt.title('Смещенные и центральные точки с погрешностями')
plt.xlabel('x')
plt.ylabel('y')

plt.legend(loc='best')

plt.show()