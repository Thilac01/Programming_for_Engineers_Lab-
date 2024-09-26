import matplotlib.pyplot as plt
import numpy as np

class Graphs:
    def __init__(self, labels, values, colors):
        self.labels = labels
        self.values = values
        self.colors = colors

    def pie_chart(self, title, fontsize):
        plt.subplot(1, 2, 1)  # Create the first subplot for pie chart
        plt.pie(self.values, labels=self.labels, colors=self.colors, autopct='%1.1f%%')
        plt.title(title, fontsize=fontsize)

    def bar_chart(self, x_label, y_label, title):
        plt.subplot(1, 2, 2)  # Create the second subplot for bar chart
        x = np.arange(len(self.labels))  # Use dynamic length of labels for x-axis
        plt.bar(x, self.values, color=self.colors)
        plt.xticks(x, self.labels, fontsize=12)
        plt.ylabel(y_label, fontsize=13)
        plt.xlabel(x_label, fontsize=13)
        plt.title(title, fontsize=14)

    def display_charts(self, pie_title, pie_fontsize, bar_x_label, bar_y_label, bar_title):
        plt.figure(figsize=(12, 6)) 
        self.pie_chart(pie_title, pie_fontsize)
        self.bar_chart(bar_x_label, bar_y_label, bar_title)
        plt.show()

if __name__ == '__main__':
    graph = Graphs(
        ["Apples", "Bananas", "Cherries", "Dates"],
        [30, 20, 5, 25],
        ["#7DDA58", "#FFD736", "#5DE2E7", "#CF8788"]
    )
    
    # Display the pie and bar charts with appropriate titles and labels
    graph.display_charts("Fruit Distribution", 16, "Fruits", "Quantity", "Fruit Bar Chart")
