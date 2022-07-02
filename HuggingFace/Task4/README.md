Let's edit the ".yaml" files

This step is similar to deploying your frontend application to your cluster:

Ref: [#4 Week SE Weekly - Deploying to your cluster](https://docs.google.com/presentation/d/1Hk8CecrDcgh_yXvWd-XO-WeOFi7Ta6vjdo-Fn3Pqwsk/edit#slide=id.g12fa92489d1_0_0)

- Put **deployment.yaml** inside your "ai server" dir

- Put **ai.yml** inside /.github/workflows

- For **build-and-deploy.yml** file

  - Put it inside /.github/workflows

- look for this part(it's at the end of the file)

```bash
  name: get IP address of deployment
  run: kubectl get services --namespace development frontend --output jsonpath='{.status.loadBalancer.ingress[0].ip}'
```

- and change it to this

```bash
name: get IP address of deployment
run: kubectl get services --namespace development ${{ inputs.image-name }} --output jsonpath='{.status.loadBalancer.ingress[0].ip}'
```
