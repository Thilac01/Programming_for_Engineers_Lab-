# CO1010 Lab 07
# Pie chart
# Import libraries
import matplotlib.pyplot as plt
# Plot labels
labels = ["Very Easy", "Easy", "Moderate", "Difficult", "Very Difficult"]
# data (statistics)
sizes = [0.74 ,5.46, 55.33 , 34.99 ,3.47]
# colours
colors = ["yellowgreen", "gold", "lightskyblue", "lightcoral", "b"]
# plot setup
patches , texts = plt.pie(sizes , colors=colors , shadow=True , startangle
=90)
plt.legend(patches , labels , loc="best")
plt.axis("equal")
plt.title("CO1010 Labs",fontsize =14)
plt.show()