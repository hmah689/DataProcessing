import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Define the exponential function
def exponential(x, a, b):
    return a * np.exp(b * x)


# Initialize lists to store AC data
data_0AC = []
data_50AC = []
data_100AC = []
data_150AC = []
data_200AC = []

# Open the file and read its contents
with open('AllTests.txt', 'r') as file:
    for line in file:
        data = line.split()
        if len(data) == 0 or data[0] == 'Force':
            continue  # Skip empty lines or header lines
        try:
            force_value = float(data[0])  # Convert the first element to a float
            if force_value == 0:
                data_0AC.append(data[1:])  # Append the rest of the line
            elif force_value == 50:
                data_50AC.append(data[1:])
            elif force_value == 100:
                data_100AC.append(data[1:])
            elif force_value == 150:
                data_150AC.append(data[1:])
            elif force_value == 200:
                data_200AC.append(data[1:])
        except ValueError:
            print(f"Could not convert line to float: {line.strip()}")  # Handle potential conversion errors

dc_values = [2, 3, 4, 5, 6, 7, 8, 9, 10]  # DC values for x-axis

dc_2a = []
dc_3a = []
dc_4a = []
dc_5a = []
dc_6a = []
dc_7a = []
dc_8a = []
dc_9a = []
dc_10a = []
for x in range(0,5):
    if x == 0:
        for line in data_0AC:
            dc_2a.append(float(line[0]))
            dc_3a.append(float(line[1]))
            dc_4a.append(float(line[2]))
            dc_5a.append(float(line[3]))
            dc_6a.append(float(line[4]))
            dc_7a.append(float(line[5]))
            dc_8a.append(float(line[6]))
            dc_9a.append(float(line[7]))
            dc_10a.append(float(line[8]))
        data_zip_0AC = [dc_2a,dc_3a,dc_4a,dc_5a,dc_6a,dc_7a,dc_8a,dc_9a,dc_10a]

    if x == 1:
        for line in data_50AC:
            dc_2a.append(float(line[0]))
            dc_3a.append(float(line[1]))
            dc_4a.append(float(line[2]))
            dc_5a.append(float(line[3]))
            dc_6a.append(float(line[4]))
            dc_7a.append(float(line[5]))
            dc_8a.append(float(line[6]))
            dc_9a.append(float(line[7]))
            dc_10a.append(float(line[8]))
        data_zip_50AC = [dc_2a,dc_3a,dc_4a,dc_5a,dc_6a,dc_7a,dc_8a,dc_9a,dc_10a]

    if x == 2:
        for line in data_100AC:
            dc_2a.append(float(line[0]))
            dc_3a.append(float(line[1]))
            dc_4a.append(float(line[2]))
            dc_5a.append(float(line[3]))
            dc_6a.append(float(line[4]))
            dc_7a.append(float(line[5]))
            dc_8a.append(float(line[6]))
            dc_9a.append(float(line[7]))
            dc_10a.append(float(line[8]))
        data_zip_100AC = [dc_2a,dc_3a,dc_4a,dc_5a,dc_6a,dc_7a,dc_8a,dc_9a,dc_10a]

    if x == 3:
        for line in data_150AC:
            dc_2a.append(float(line[0]))
            dc_3a.append(float(line[1]))
            dc_4a.append(float(line[2]))
            dc_5a.append(float(line[3]))
            dc_6a.append(float(line[4]))
            dc_7a.append(float(line[5]))
            dc_8a.append(float(line[6]))
            dc_9a.append(float(line[7]))
            dc_10a.append(float(line[8]))
        data_zip_150AC = [dc_2a,dc_3a,dc_4a,dc_5a,dc_6a,dc_7a,dc_8a,dc_9a,dc_10a]

    if x == 4:
        for line in data_200AC:
            dc_2a.append(float(line[0]))
            dc_3a.append(float(line[1]))
            dc_4a.append(float(line[2]))
            dc_5a.append(float(line[3]))
            dc_6a.append(float(line[4]))
            dc_7a.append(float(line[5]))
            dc_8a.append(float(line[6]))
            dc_9a.append(float(line[7]))
            dc_10a.append(float(line[8]))
        # dc_2a.remove(dc_2a[4])
        # dc_3a.remove(dc_3a[4])
        # dc_4a.remove(dc_4a[4])
        data_zip_200AC = [dc_2a,dc_3a,dc_4a,dc_5a,dc_6a,dc_7a,dc_8a,dc_9a,dc_10a]

    x += 1
    dc_2a = []
    dc_3a = []
    dc_4a = []
    dc_5a = []
    dc_6a = []
    dc_7a = []
    dc_8a = []
    dc_9a = []
    dc_10a = []

data = {
    0: data_zip_0AC,
    50: data_zip_50AC,
    100: data_zip_100AC,
    150: data_zip_150AC,
    200: data_zip_200AC
}

# data = {
#     50: data_zip_50AC,
# }




# Define colors for each force level
colors = ['blue', 'orange', 'green', 'red', 'purple']


# Loop through each force value and its corresponding data
for idx, (force, ac_values_list) in enumerate(data.items()):
    # Create a scatter plot
    plt.figure(figsize=(10, 6))

    # Prepare lists for scatter plotting
    x_values = []
    y_values = []
    
    for dc_value, ac_values in zip(dc_values, ac_values_list):
        for ac_value in ac_values:  # Loop through multiple AC measurements
            x_values.append(dc_value)
            y_values.append(float(ac_value))  # Ensure AC values are floats
    
    # Scatter plot for the current force
    color = colors[idx]  # Select color based on index
    plt.scatter(x_values, y_values, label=f'Force = {force} N', alpha=0.7, color=color)

    # Calculate and plot the trendline
    if x_values and y_values:  # Check if there are data points
    # Fit the exponential model to the data
        params, _ = curve_fit(exponential, x_values, y_values)

        # Generate x values for the trendline
        x_fit = np.linspace(min(x_values), max(x_values), 100)
        y_fit = exponential(x_fit, *params)

        # Plot the trendline
        plt.plot(x_fit, y_fit, linestyle='--', color=color)


        # Calculate R²
        y_pred = exponential(np.array(x_values), *params)
        ss_res = np.sum((y_values - y_pred) ** 2)  # Residual sum of squares
        ss_tot = np.sum((y_values - np.mean(y_values)) ** 2)  # Total sum of squares
        r_squared = 1 - (ss_res / ss_tot)

        # Determine the position to display R^2
        offset = -1.9 # Adjust the offset based on the index
        plt.text(4.2,55.5+idx*offset,f'$R^2 = {r_squared:.2f}$', color=color, fontsize=10, ha='center')
        
        # Create the equation string
        a, b = params  # a and b are the coefficients for the exponential fit
        equation = f'$y = {a:.2f} e^{{{b:.2f} x}}$'

        # Display the equation on the plot
        plt.text(6, 55.5 + idx * offset, equation, color=color, fontsize=10, ha='center')

    # Adding labels and title
    plt.title('Scatter Plot of Force vs. DC Values with Multiple Measurements')
    plt.xlabel('DC Values')
    plt.ylabel('AC Values')
    plt.xticks(dc_values)  # Set x-ticks to DC values
    plt.legend()
    plt.grid(True)

    # Save the plot as a file and show it
    plt.savefig(f"{idx}.png")
    plt.show()