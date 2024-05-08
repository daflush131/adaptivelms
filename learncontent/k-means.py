import random

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

    return clusters

# Sample function to gather student data from Django model
def get_student_data():
    # Assuming each student's data is in the format [total_score, total_correct_items]
    student_data = [
        [85, 20],
        [70, 15],
        [90, 25],
        [60, 10],
        [95, 30],
        [55, 12]
    ]
    return student_data

# Function to perform clustering and associate students with clusters
def perform_clustering(k):
    # Get student data
    student_data = get_student_data()

    # Perform k-means clustering
    clusters = k_means(student_data, k)

    # Sort clusters based on average score and average number of correct items
    sorted_clusters = sorted(clusters, key=lambda x: (sum(p[0] for p in x) / len(x), sum(p[1] for p in x) / len(x)))

    # Associate each student with a cluster
    student_cluster_mapping = {}
    for i, cluster in enumerate(sorted_clusters):
        for student in cluster:
            student_cluster_mapping[tuple(student)] = i + 1  # Cluster numbering starts from 1

    return student_cluster_mapping

# Example usage:
num_clusters = 3
student_cluster_mapping = perform_clustering(num_clusters)

# Print the mapping of each student to their cluster
for student, cluster in student_cluster_mapping.items():
    print(f"Student with data {student} belongs to Cluster {cluster}")
