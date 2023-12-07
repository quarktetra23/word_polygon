import matplotlib.pyplot as plt
import numpy as np

def draw_polygon(n_sides):
    angles = np.linspace(0, 2 * np.pi, n_sides, endpoint=False)
    x = np.cos(angles)
    y = np.sin(angles)
    return np.append(x, x[0]), np.append(y, y[0])  # Append the first point to the end to close the loop

def calculate_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def shoelace_area(coords):
    x = coords[:, 0]
    y = coords[:, 1]
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))

def plot_word(word, x, y):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letter_offset = 1.1  # Increase this value to move letters further out
    positions = {letter: (x[i], y[i]) for i, letter in enumerate(alphabet)}

    # Plot all letters around the polygon with an offset
    for i, letter in enumerate(alphabet):
        offset_x, offset_y = x[i] * letter_offset, y[i] * letter_offset
        plt.text(offset_x, offset_y, letter.upper(), fontsize=12, ha='center', va='center')

    prev_char = word[0].lower()
    plt.plot(x, y, marker='o')

    total_length = 0
    word_coords = []
    for char in word.lower():
        if char != prev_char:
            plt.plot(*zip(*[positions[prev_char], positions[char]]), marker='o')
            total_length += calculate_distance(positions[prev_char], positions[char])
            word_coords.append(positions[char])
        prev_char = char

    # Calculate the area if the word forms a closed shape
    if len(word_coords) > 2:
        enclosed_area = shoelace_area(np.array(word_coords))
    else:
        enclosed_area = 0

    # Mark the origin with a unique color
    plt.scatter(0, 0, color='magenta', marker='x')

    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(f"Total Length of Path: {total_length:.2f}, Enclosed Area: {enclosed_area:.2f}")
    plt.show()

# Main
n_sides = 26
x, y = draw_polygon(n_sides)
word = input("Enter a word: ")
plot_word(word, x, y)
