import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def fibonacci_ratios(fib_sequence):
    ratios = []
    for i in range(2, len(fib_sequence)):
        ratios.append(fib_sequence[i] / fib_sequence[i-1])
    return ratios

def plot_fibonacci_spiral(fib_sequence, factor, ax):
    x, y, direction = 0, 0, 0
    for i, size in enumerate(fib_sequence[2:]):
        # Draw squares
        rect = patches.Rectangle((x, y), size*factor, size*factor, linewidth=1, edgecolor='blue', facecolor='none')
        ax.add_patch(rect)
        
        # Calculate next position and draw spiral arcs
        if direction % 4 == 0:
            arc_start = (x + size*factor, y)
            x += size*factor
        elif direction % 4 == 1:
            arc_start = (x, y + size*factor)
            y += size*factor
        elif direction % 4 == 2:
            arc_start = (x - size*factor, y)
            x -= fib_sequence[i]*factor
            y -= size*factor - fib_sequence[i]*factor
        elif direction % 4 == 3:
            arc_start = (x, y - size*factor)
            x += fib_sequence[i+1]*factor
            y -= fib_sequence[i+1]*factor
        
        # Adjust arc drawing to cover 90 degrees from arc_start, in the correct direction
        for angle in range(90):
            radians = np.radians(angle + direction * 90)
            arc_x = arc_start[0] + size*factor*np.cos(radians) * (-1 if direction % 2 == 0 else 1)
            arc_y = arc_start[1] + size*factor*np.sin(radians) * (1 if direction % 2 == 0 else -1)
            ax.plot(arc_x, arc_y, 'r-', linewidth=0.5)

        direction += 1

# Generate the first 20 Fibonacci numbers
n = 20
fib_sequence = fibonacci(n)
ratios = fibonacci_ratios(fib_sequence)

# Set up the plot area
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Fibonacci Sequence Graph
axs[0].bar(range(n), fib_sequence, color='skyblue')
axs[0].set_title('Fibonacci Sequence')
axs[0].set_xlabel('Index')
axs[0].set_ylabel('Fibonacci Number')

# Ratio of Consecutive Fibonacci Numbers
axs[1].plot(range(2, n), ratios, marker='o', linestyle='-', color='orange')
axs[1].set_title('Ratio of Consecutive Fibonacci Numbers')
axs[1].set_xlabel('Index')
axs[1].set_ylabel('Ratio')
axs[1].axhline(y=1.61803398875, color='r', linestyle='--', label='Golden Ratio (~1.618)')
axs[1].legend()

# Fibonacci Spiral Graph
ax = axs[2]
plot_fibonacci_spiral(fib_sequence, 1, ax)
ax.set_title('Fibonacci Spiral')
ax.axis('equal')

plt.tight_layout()
plt.show()
