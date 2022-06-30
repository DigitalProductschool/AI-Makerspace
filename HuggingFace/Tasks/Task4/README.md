Let's edit the ".yaml" files

This step is similar to deploying your frontend application to your cluster:

Ref: [#4 Week SE Weekly - Deploying to your cluster](https://docs.google.com/presentation/d/1Hk8CecrDcgh_yXvWd-XO-WeOFi7Ta6vjdo-Fn3Pqwsk/edit#slide=id.g12fa92489d1_0_0)

1. In **deployment.yaml** file:

- change every instance of "frontend" to "ai"
- change the port numbers to the port your ai application uses
- change "dockerfile" param to your Dockerfile's name
- Put this file(deployment.yaml) inside your "ai server" dir

2. In **ai.yml** file

- change the "paths" parameter to the path of your "ai server" dir.
  Ex: **"ai-fastapi-server/\*\*"**
- change the **cluster-name** to your cluster's name Ex.: "farmpedia"
- change **repository** name. Ex: "batch16--farmpedia"
- Put **ai.yml** inside the /.github/workflows

3. In **build-and-deploy.yml** file

- look for this part(it's at the end)

```bash
  name: get IP address of deployment
  run: kubectl get services --namespace development frontend --output jsonpath='{.status.loadBalancer.ingress[0].ip}'
```

- and change it to this

```bash
name: get IP address of deployment
run: kubectl get services --namespace development ${{ inputs.image-name }} --output jsonpath='{.status.loadBalancer.ingress[0].ip}'
```
