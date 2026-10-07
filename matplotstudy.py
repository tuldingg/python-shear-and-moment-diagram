import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize = (10,3))        # Create a blank canvas
ax.grid(True)
ax.set_ylim(-1, 3)   # Force y-axis from -1 to 3
ax.yaxis.set_visible(False) 
ax.plot([0, 10], [0, 0])        # Draw a line from (0,0) to (10,0)
ax.plot(0, 0, marker='^', color='green', markersize=10)  
ax.plot(10, 0, marker='o', color='green', markersize=10)  
ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ax.annotate('', xy=(3, 0), xytext=(3, 1),
            arrowprops=dict(arrowstyle='->', color='red'))
ax.text(3, 1, '50 kN', ha='center', color='red')


plt.show()
