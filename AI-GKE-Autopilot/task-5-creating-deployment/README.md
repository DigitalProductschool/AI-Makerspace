# Creating Deployment

In task-6, we are going to follow these steps:

1. Make `kubectl` alias, using:
```bash
alias k=kubectl
```
2. Deploy the `deployment.yaml` manifest file, using:
```bash
k create -f $WORKING_DIR/task-5-creating-deployment/deploy.yaml
```
2. Watch the deployment status, using:
```bash
k get deploy --watch
```