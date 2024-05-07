import pandas as pd
import matplotlib.pyplot as plt


# reading the database
data = pd.read_csv("C:\\Users\\LENOVO\\Documents\\KULIAH\\Semester 6\\Data Visualisasi\\tips.csv")

# Scatter plot with day against tip
plt.plot(data['tip'])
plt.plot(data['size'])

# Adding Title to the Plot
plt.title("Scatter Plot")

# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')

plt.show()
