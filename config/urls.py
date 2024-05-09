from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from accounts.views import CustomLoginView
from learncontent.kmeans import perform_clustering

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls', )),
    path('remotelab/', include('remotelab.urls')),
    path('lessons/', include('learncontent.urls')),


    path('', CustomLoginView.as_view(), name='root_redirect'),
]

database_data = [
        [222, 85, 20],
        [233, 70, 15],
        [100, 90, 25],
        [344, 60, 10],
        [343, 95, 30],
        [643, 55, 12]
    ]

num_clusters = 3
student_cluster_mapping = perform_clustering(num_clusters,database_data)

## Initialize an empty list to store the data
data = []
# Loop through the student_cluster_mapping dictionary
for user_id, cluster in student_cluster_mapping.items():
    # Append the user_id and cluster as a list to the data list
    data.append([user_id, cluster]) 
print(data)

