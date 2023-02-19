import matplotlib.pyplot as plt
import numpy as np

# Generate random sales data for 12 months
sales_data = np.random.randint(low=100, high=1000, size=(12))

# Create a list of months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Plot the sales data as a line graph
plt.plot(months, sales_data)

# Set the title and labels for the graph
plt.title('Business Sales over Time')
plt.xlabel('Months')
plt.ylabel('Sales')

# Display the graph
plt.show()
