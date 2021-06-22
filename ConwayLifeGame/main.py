import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


def create_initial_grid(m, n):
    return np.random.randint(2, size=(m, n))


def get_neighbours(row, col, M):
    life_sum = 0
    shape = len(M), len(M[0])
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                life_sum += M[((row + i) % shape[0])][((col + j) % shape[1])]
    return life_sum


def iterate_numpy(M):
    shape = len(M), len(M[0])
    K = [[0, ] * (shape[1]) for i in range(shape[0])]
    for row in range(shape[0]):
        for col in range(shape[1]):
            live_neighbors = get_neighbours(row, col, M)
            if live_neighbors < 2 or live_neighbors > 3:
                K[row][col] = 0
            elif live_neighbors == 3 and M[row][col] == 0:
                K[row][col] = 1
            else:
                K[row][col] = M[row][col]
    return K


def animate(data):
    global M
    Z = M.copy()
    for i in range(10):
        Z = iterate_numpy(M)
        mat.set_data(Z)
        M = Z
        if M == Z:
            break
    return [mat]


if __name__ == '__main__':
    M = create_initial_grid(20, 20)
    print(M)

    # set up animation
    fig, ax = plt.subplots()
    mat = ax.matshow(M)
    ani = animation.FuncAnimation(fig, animate, interval=50, save_count=50)
    plt.show()
