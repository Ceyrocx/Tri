import matplotlib.pyplot as plt
import numpy as np
from math import ceil

# amount = 150
#
# L = np.random.randint(0, 100, amount)
# x = np.arange(0, amount, 1)

def visualisation(L, verif, time=0.01, legende=None, nbTest=None):
    n = len(L)
    x = np.arange(1, n+1, 1)

    # for i in range(n):
    #     for j in range(0, n-i-1):
    plt.pause(time)
    plt.clf()

    plt.subplots_adjust(top=0.85)
    plt.title(legende, color="orange", loc="center", fontweight="bold")
    # title_y = plt.gca().get_title().get_position()[1]

    plt.text(x=1, y=1.022, s=f"Test n°{nbTest}", ha="right", fontsize=10, transform=plt.gca().transAxes)
    plt.bar(x, L, color="orange")


    if verif == True:
        plt.show()
