import numpy as np  # Importing NumPy library for numerical operations
import matplotlib.pyplot as plt  # Importing Matplotlib for plotting

x = np.linspace(0, 10, 50)  # Creating an array of 50 points from 0 to 10
y = np.cos(x)  # Calculating the cosine of each point in the array x

# Plotting x vs y with specified styling:
# 'o' denotes circular markers, linestyle is dashed ('--'), color is red,
# markersize is 5, and alpha (transparency) is set to 0.5
plt.plot(x, y, 'o', linestyle='--', color='red', markersize=5, alpha=0.5)

plt.xlabel('x-axis')  # Label for the x-axis
plt.ylabel('y-axis')  # Label for the y-axis
plt.title('Basic Line Plot')  # Title of the plot
plt.show()  # Display the plot