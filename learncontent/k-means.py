import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def generate_random_data(num_points, num_clusters=3):
    np.random.seed(42)
    data = []
    for _ in range(num_clusters):
        center = np.random.rand() * 10  # Use a single random value for the center
        cluster = center + np.random.uniform(1, 5, size=(num_points // num_clusters,))
        data.append(cluster)
    return np.concatenate(data)

def k_means(data, k=3, max_iters=100):
    data = data.reshape(-1, 1)  # Reshape to make it 2D
    # Randomly initialize centroids
    centroids = np.random.choice(data.flatten(), k, replace=False)

    for _ in range(max_iters):
        # Assign each data point to the nearest centroid
        labels = np.argmin(np.abs(data - centroids), axis=1)

        # Update centroids based on the mean of assigned data points
        new_centroids = np.array([data[labels == i].mean() for i in range(k)])

        # Check for convergence
        if np.all(centroids == new_centroids):
            break

        centroids = new_centroids

    return centroids, labels

def plot_clusters(data, centroids, labels):
    unique_labels = np.unique(labels)
    colors = plt.cm.viridis(np.linspace(0, 1, len(unique_labels)))

    for label, color in zip(unique_labels, colors):
        cluster_points = data[labels == label]
        plt.scatter(cluster_points.flatten(), np.zeros_like(cluster_points), c=color, alpha=0.7, edgecolors='k', label=f'Cluster {label}')

    plt.scatter(centroids.flatten(), np.zeros_like(centroids), c='red', marker='X', s=200, label='Centroids')
    plt.title('K-Means Clustering')
    plt.xlabel('Pre-test Scores')
    plt.legend()
    plt.show()

# Generate random data within the range [1, 10]
random_data = generate_random_data(10)

# Perform k-means clustering
k_value = 3  # You can change this value
final_centroids, cluster_labels = k_means(random_data, k=k_value)

# Plot the results
plot_clusters(random_data, final_centroids, cluster_labels)
