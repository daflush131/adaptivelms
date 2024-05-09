
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
    # Assuming each student's data is in the format [user_id, total_score, total_correct_items]
    student_data_with_id = [
        [222, 85, 20],
        [233, 70, 15],
        [100, 90, 25],
        [344, 60, 10],
        [343, 95, 30],
        [643, 55, 12]
    ]
    
    return student_data_with_id

def perform_clustering(k):
    # Get student data
    student_data_with_id = get_student_data()

    # Extract only the score and correct items for clustering
    student_data = [[score, correct_items] for _, score, correct_items in student_data_with_id]

    # Perform k-means clustering
    clusters = k_means(student_data, k)

    # Sort clusters based on average score and average number of correct items
    sorted_clusters = sorted(clusters, key=lambda x: (sum(p[0] for p in x) / len(x), sum(p[1] for p in x) / len(x)))

    # Associate each student with a cluster using user ID
    student_cluster_mapping = {}
    for i, cluster in enumerate(sorted_clusters):
        for score, correct_items in cluster:
            # Since there's no user_id in the cluster, we don't need to unpack it
            # Instead, we'll directly use the user_id from the student_data_with_id list
            user_id = next(data[0] for data in student_data_with_id if data[1:] == [score, correct_items])
            student_cluster_mapping[user_id] = i + 1  # Cluster numbering starts from 1

    return student_cluster_mapping

# Example usage:
num_clusters = 3
student_cluster_mapping = perform_clustering(num_clusters)
## Initialize an empty list to store the data
data = []

# Loop through the student_cluster_mapping dictionary
for user_id, cluster in student_cluster_mapping.items():
    # Append the user_id and cluster as a list to the data list
    data.append([user_id, cluster])
print(data)