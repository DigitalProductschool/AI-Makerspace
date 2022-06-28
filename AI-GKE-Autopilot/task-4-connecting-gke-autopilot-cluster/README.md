# Connecting GKE-Autopilot Cluster

In this task, we are going to follow these steps:

1. To view all clusters in your default zone:
```bash
gcloud container clusters list
```
2. Set the `CLUSTER_NAME` environment variable using:
```bash
export CLUSTER_NAME=<your-cluster-name>
```
3. Connect to your cluster using:
```bash
gcloud container clusters get-credentials $CLUSTER_NAME \
    --region us-west1 \
    --project=$PROJECT_ID
```
Reference: https://cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster