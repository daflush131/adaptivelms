import random
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Function to calculate the Euclidean distance between two points
def euclidean_distance(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5

# K-means clustering function
def k_means(data, k, max_iterations=100):
    # Randomly initialize centroids
    centroids = random.sample(data, k)

    for _ in range(max_iterations):
        # Assign points to nearest centroid
        clusters = [[] for _ in range(k)]
        for point in data:
            distances = [euclidean_distance(point, centroid) for centroid in centroids]
            cluster_index = distances.index(min(distances))
            clusters[cluster_index].append(point)

        # Update centroids
        new_centroids = [[sum(dim) / len(cluster) for dim in zip(*cluster)] for cluster in clusters]

        # Check for convergence
        if centroids == new_centroids:
            break

        centroids = new_centroids

    return clusters, centroids

# Function to plot clusters and centroids
def plot_clusters(clusters, centroids, lesson):
    plt.clf()
    colors = ['r', 'g', 'b', 'c', 'm', 'y']
    for i, cluster in enumerate(clusters):
        x = [point[0] for point in cluster]
        y = [point[1] for point in cluster]
        plt.scatter(x, y, c=colors[i], label=f'Cluster {i+1}')
    
    # Plot centroids
    for i, centroid in enumerate(centroids):
        plt.scatter(centroid[0], centroid[1], marker='x', c='black', label=f'Centroid {i+1}', s=100)
    
    plt.xlabel('Total Score')
    plt.ylabel('Total Correct Items')
    plt.title('K-means Clustering of Student Data for ' + lesson)
    plt.legend()
    plt.grid(True)
    plt.show()
    save_path = rf'C:\Users\marcp\Downloads\{lesson}.png'
    plt.savefig(save_path)

# Function to perform clustering and associate students with clusters
def perform_clustering(k, student_data):
    clusters, centroids = k_means(student_data, k)
    
    # Sort clusters based on some criterion (e.g., the mean value of each cluster)
    clusters = sorted(clusters, key=lambda cluster: sum(sum(dim) for dim in cluster))
    
    # Associate each student with a cluster
    student_cluster_mapping = {}
    for i, cluster in enumerate(clusters):
        for student in cluster:
            student_cluster_mapping[tuple(student)] = i + 1  # Cluster numbering starts from 1

    return clusters, centroids, student_cluster_mapping 