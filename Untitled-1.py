from google.cloud import storage
from google.auth import default

# Step 1: Authenticate with Google Cloud
credentials, project_id = default()

# Step 2: Initialize the Google Cloud Storage client
client = storage.Client(credentials=credentials, project=project_id)

# Step 3: List all buckets in the project
buckets = client.list_buckets()

print(f"Buckets in project {project_id}:")
for bucket in buckets:
    print(f"- {bucket.name}")
