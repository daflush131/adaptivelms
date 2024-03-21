import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def generate_pretest_score(num_points, num_clusters=3):
    np.random.seed(42)
    data = []
    for _ in range(num_clusters):
        center = np.random.rand() * 50  # Use a single random value for the center
        cluster = center + np.random.uniform(1, 5, size=(num_points // num_clusters,))
        data.append(cluster)
    return np.concatenate(data)

def k_means_sklearn(data, k=3):
    data = data.reshape(-1, 1)  # Reshape to make it 2D

    # Use scikit-learn's KMeans
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(data)
    centroids = kmeans.cluster_centers_

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

score = 40
# Generate random data within the range [1, 10]

pretest_score = generate_pretest_score(40)

# Perform k-means clustering using scikit-learn's KMeans
k_value = 3  # You can change this value
final_centroids, cluster_labels = k_means_sklearn(pretest_score, k=k_value)

# Plot the results
plot_clusters(pretest_score, final_centroids, cluster_labels)
