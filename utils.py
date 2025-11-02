from scipy.cluster.hierarchy import dendrogram
import matplotlib.pyplot as plt

def plot_dendogram(linkage_matrix, title='Dendogram'):
    plt.figure()

    print('aaaaaaa', linkage_matrix)

    dendrogram(linkage_matrix)

    plt.title(title)
    plt.xlabel('Sample index')
    plt.ylabel('Distance')
    plt.show()
