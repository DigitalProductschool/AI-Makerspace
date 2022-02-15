To deploy:

```
$ gcloud init
$ gcloud config set app/cloud_build_timeout 3000
$ gcloud app deploy --log-http
```