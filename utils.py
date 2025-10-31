from scipy.cluster.hierarchy import dendrogram
import matplotlib.pyplot as plt

def plot_dendogram(linkage_matrix, title='Dendogram'):
    plt.figure()

    dendrogram(linkage_matrix)

    plt.title(title)
    plt.xlabel('Sample index')
    plt.ylabel('Distance')
    plt.show()
