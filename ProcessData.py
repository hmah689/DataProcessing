import matplotlib.pyplot as plt
import numpy as np

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

# Create a scatter plot
plt.figure(figsize=(10, 6))
# Define colors for each force level
colors = ['blue', 'orange', 'green', 'red', 'purple']

# Loop through each force value and its corresponding data
for idx, (force, ac_values_list) in enumerate(data.items()):
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
        # Fit a polynomial of degree 2 (quadratic) to better capture the trend
        z = np.polyfit(x_values, y_values, 2)  # Change to 2 for a quadratic fit
        p = np.poly1d(z)  # Create a polynomial function

        # Generate x values for the trendline
        x_fit = np.linspace(min(x_values), max(x_values), 100)
        plt.plot(x_fit, p(x_fit), linestyle='--', color=color)  # Plot the trendline with the same color

# Adding labels and title
plt.title('Scatter Plot of Force vs. DC Values with Multiple Measurements')
plt.xlabel('DC Values')
plt.ylabel('AC Values')
plt.xticks(dc_values)  # Set x-ticks to DC values
plt.legend()
plt.grid(True)

# Save the plot as a file and show it
plt.savefig("force_vs_dc_scatter_multiple_measurements_with_colored_trendlines.png")
plt.show()