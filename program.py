
# Data Visualization using Matplotlib
# Matplotlib is a widely used data visualization library in Python that provides a variety of tools for creating static, animated, and interactive visualizations. It is built on top of NumPy and is designed to work seamlessly with other libraries such as Pandas and SciPy. Matplotlib allows users to create a wide range of plots and charts, including line plots, scatter plots, bar charts, histograms, pie charts, and more. It offers extensive customization options for controlling the appearance of plots, including colors, labels, titles, and axes. Matplotlib is commonly used in data analysis, scientific research, and machine learning to visualize data patterns and insights effectively.
# In this code, we will explore various types of plots and charts using Matplotlib to visualize different aspects of a dataset. We will cover univariate analysis for both numerical and categorical data, bivariate analysis for numerical and categorical combinations, and multivariate analysis involving multiple variables. Additionally, we will utilize the object-oriented API of Matplotlib to create more complex visualizations. Finally, we will also demonstrate how to create a 3D plot to visualize three-dimensional data.
# Importing necessary libraries
# %matplotlib inline

import matplotlib.pyplot as plt # For plotting
import pandas as pd # For data manipulation
import numpy as np  # Import NumPy for numerical operations

# Simple line plot
x = [1,2,3]
y = [4,5,6]
plt.plot(x,y)
plt.grid()
plt.show()

# Simple scatter plot
plt.scatter(x,y)
plt.grid()
plt.show()

# Pypolt API
# Univarite - Numerical

data = {
    "Salary" : [25000,30000,37000,28000,39000,48000,52000,35000,58000] # Salary of 9 employees
}
df = pd.DataFrame(data)
print(df.head())
print(df.shape)

# Line Plot:
plt.plot(df["Salary"],color = "red", marker = "o", linestyle = ":", linewidth = "2") # Line plot with red color, circle markers, dotted line style, and line width of 2
plt.show()

# Histogram

plt.hist(df["Salary"], bins= 5, color="green" ) # Histogram with 5 bins and green color
plt.show()

# Boxplot:
plt.boxplot(df["Salary"]) # Boxplot to visualize the distribution of Salary
plt.show()

# Univaritate: Categorical
df["dept"] = ["HR","IT","HR","HR","Finance","IT","HR","IT","Finance"] # Department of each employee
print(df.head())
print(df.shape)

# Pie chart
count = df["dept"].value_counts() # Count the number of occurrences of each department
plt.pie(count, labels= count.index,autopct="%1.2f", explode=[0,0.1,0.2]) # Pie chart with labels, percentage display, and explode effect
plt.show()

# Countplot

plt.bar(count.index, count, color = ["green","red","orange"]) # Bar chart to show the count of each department with specified colors
plt.show()

# Bivariate - numerical - numerical:
df["Age"] = [22,24,26,24,23,21,25,26,21] # Age of each employee
print(df.head())

# Scatter plot
plt.scatter(df["Age"],df["Salary"],color = "red") # Scatter plot to visualize the relationship between Age and Salary with red color
plt.savefig("Scatterplot.png") # Save the scatter plot as a PNG file
plt.show()
sort_age = df.sort_values("Age") # Sort the DataFrame by Age to create a line plot with sorted ages
# Line plot:
plt.plot(sort_age["Age"],df["Salary"],color = "red", marker = "*", linestyle = ":", linewidth = "2") # Line plot with sorted ages, red color, star markers, dotted line style, and line width of 2
plt.grid()
plt.savefig("LinePlot.png") # Save the line plot as a PNG file
plt.show()

# Bar chart:
plt.bar(sort_age["Age"],df["Salary"], color = "green") # Bar chart to show the relationship between Age and Salary with green color
plt.show()

# Bivariate : Numerical - categorical:
hr_sal = df[df["dept"] == "HR"]["Salary"]
it_sal = df[df["dept"] == "IT"]["Salary"]
fin_sal = df[df["dept"] == "Finance"]["Salary"] # Extract Salary values for each department (HR, IT, Finance) to create boxplots and bar charts for categorical analysis
# Boxplot:
plt.boxplot([hr_sal, it_sal, fin_sal], label=["HR","IT","Finance"]) # Boxplot to compare the distribution of Salary across different departments (HR, IT, Finance) with labels
plt.legend() # Add legend to the boxplot
plt.savefig("Boxplot.png")
plt.show()

# Pie chart

salary_by_dept = df.groupby("dept")["Salary"].sum() # Total salary in work in HR dept
print(salary_by_dept)
plt.pie(salary_by_dept, labels= salary_by_dept.index,autopct="%1.2f",shadow=True,explode=[0.1,0,0]) # Pie chart to show the proportion of total Salary by department with labels, percentage display, shadow effect, and explode effect for HR department
plt.axis("equal") # Equal aspect ratio to ensure the pie chart is circular
plt.savefig("Piechart.png")
plt.show()
# Bar plot
hr_mean = sum(hr_sal)/len(hr_sal) # Average salary in HR department
it_mean = sum(it_sal)/len(it_sal)
fin_mean = sum(fin_sal)/len(fin_sal)
plt.bar(["HR","IT","Finance"],[hr_mean,it_mean,fin_mean], color =["green","red","blue"]) # Bar chart to compare the average Salary across different departments (HR, IT, Finance) with specified colors
plt.grid()
plt.savefig("Barchart.png")
plt.show()

# Multivariate Analysis: 3 Numerical columns
df["Experience"] = [1,2.3,1,5,4,7,1,5,2]
print(df.head())

# Bubble Plot:
plt.scatter(df["Age"],df["Salary"],s=df["Experience"]*20,color = "orange", edgecolors="black") # Bubble plot to visualize the relationship between Age, Salary, and Experience with bubble size proportional to Experience, orange color, and black edge colors
plt.title("Age vs Salary vs Experience") # Title for the bubble plot
plt.xlabel("Age") # Label for the x-axis
plt.ylabel("Salary") # Label for the y-axis
plt.grid()
plt.show()

# 2 Numerical and 1 categorical column:
plt.scatter(df["Age"],df["Salary"],c = df["dept"].map({"HR" : "yellow","IT" : "red","Finance" : "green"})) # Scatter plot to visualize the relationship between Age and Salary with color representing the department (HR, IT, Finance) using a color mapping
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Age vs Salary vs Dept") # Title for the scatter plot
plt.legend()
plt.show()

# Object oriented API
fig, axs = plt.subplots(1,3, figsize = (10,5)) # Create a figure with 1 row and 3 columns of subplots, and set the figure size to 10 inches by 5 inches
# Line plot
axs[0].plot(sort_age["Age"], df["Salary"], color = "red", marker = "*", linewidth = "2",markersize = 2) # Line plot in the first subplot with sorted ages, red color, star markers, line width of 2, and marker size of 2
axs[0].grid()
axs[0].set_title("Line Plot") # Title for the first subplot
axs[0].set_xlabel("Age") # Label for the x-axis of the first subplot
axs[0].set_ylabel("Salary") # Label for the y-axis of the first subplot
# Histogram
axs[1].hist(df["Salary"], bins = 5, color = "green") # Histogram in the second subplot with 5 bins and green color
axs[1].set_title("Histogram") # Title for the second subplot
axs[1].set_xlabel("Salary") # Label for the x-axis of the second subplot
axs[1].set_ylabel("Frequency") # Label for the y-axis of the second subplot
# Boxplot
axs[2].boxplot(df["Salary"]) # Boxplot in the third subplot to visualize the distribution of Salary
axs[2].set_title("Boxplot") # Title for the third subplot
axs[2].set_xlabel("Salary") # Label for the x-axis of the third subplot
plt.savefig("multipleplots.png")
plt.show()
# Financial Analysis
data2 ={
    "Year":[2020,2021,2022,2023],
    "Sales":[100,150,200,250],
    "Profit":[20,30,40,50],
    "Expenses":[80,120,160,200]
}
df2 = pd.DataFrame(data2)
plt.plot(df2["Year"],df2["Sales"],label = "Sales") # Line plot to show the trend of Sales over the years with label "Sales"
plt.plot(df2["Year"],df2["Profit"],label = "Profit") # Line plot to show the trend of Profit over the years with label "Profit"
plt.plot(df2["Year"],df2["Expenses"],label = "Expenses") # Line plot to show the trend of Expenses over the years with label "Expenses"
plt.title("Financial Analysis")
plt.xlabel("Year")
plt.ylabel("Amount")
plt.legend()
plt.savefig("Financial_Analysis.png")
plt.show()

# 3-D plot
# 3D plotting in Matplotlib allows us to visualize data in three dimensions, providing a more comprehensive view of the relationships between variables. To create a 3D plot, we can use the `Axes3D` class from the `mpl_toolkits.mplot3d` module. This enables us to create various types of 3D plots, such as scatter plots, surface plots, and wireframe plots. In a 3D scatter plot, we can represent three numerical variables on the x, y, and z axes, allowing us to explore how they interact with each other in a three-dimensional space. This is particularly useful for identifying patterns and trends that may not be apparent in two-dimensional plots.

ax = plt.axes(projection = "3d") # Create a 3D axes object for plotting 3D data
# 3D Scatter Plot:
ax.scatter(df["Age"],df["Salary"],df["Experience"]) # 3D scatter plot to visualize the relationship between Age, Salary, and Experience with points in 3D space
ax.set_title("3D Scatter Plot") # Title for the 3D scatter plot
ax.set_xlabel("Age")
ax.set_ylabel("Salary")
ax.set_zlabel("Experience")
plt.savefig("3D_Plot.png")
plt.show()

# Surface Plot:

x = np.linspace(-5, 5, 100) # Generate 100 linearly spaced values for x-axis from -5 to 5
y = np.linspace(-5, 5, 100) # Generate 100 linearly spaced values for y-axis from -5 to 5
x, y = np.meshgrid(x, y) # Create a meshgrid for x and y values to create a grid of points for surface plotting
z = np.sin(np.sqrt(x**2 + y**2)) # Calculate z values using a function of x and y (in this case, a sine function based on the distance from the origin)
fig = plt.figure() # Create a new figure for the surface plot
ax = fig.add_subplot(111, projection='3d') # Add a 3D subplot to the figure
ax.plot_surface(x, y, z, cmap='viridis') # Create a surface plot with a color map
ax.set_title("Surface Plot") # Title for the surface plot
ax.set_xlabel("X") # Label for the x-axis
ax.set_ylabel("Y") # Label for the y-axis
ax.set_zlabel("Z") # Label for the z-axis
plt.savefig("Surface_Plot.png")
plt.show()

# Wireframe Plot:
fig = plt.figure() # Create a new figure for the wireframe plot
ax = fig.add_subplot(111, projection='3d') # Add a 3D subplot to the figure
ax.plot_wireframe(x, y, z, cmap='viridis') # Create a wireframe plot with a color map
ax.set_title("Wireframe Plot") # Title for the wireframe plot
ax.set_xlabel("X") # Label for the x-axis
ax.set_ylabel("Y") # Label for the y-axis
ax.set_zlabel("Z") # Label for the z-axis
plt.savefig("Wireframe_Plot.png")
plt.show()
