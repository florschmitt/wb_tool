## Push to Google Container Registry

Go to the GCP console, to Container Registry, and enable the service.

### Authenticate docker

```bash
gcloud auth configure-docker
```

### Build for deployment

You need to define your project ID.

```bash
# This section creates the necessary variables to build
export GCP_PROJECT_ID="PROJECT_ID"
export DOCKER_IMAGE_NAME="CONTAINER_NAME"
export GCR_MULTI_REGION="eu.gcr.io"
export GCR_REGION="europe-west1"

# This uses the variables to build
docker build -t $GCR_MULTI_REGION/$GCP_PROJECT_ID/$DOCKER_IMAGE_NAME .
```

### PUSH!

```bash
# Don't foget to replace with your own PROJECT_ID and CONTAINER_NAME
export GCP_PROJECT_ID="PROJECT_ID"
export DOCKER_IMAGE_NAME="CONTAINER_NAME"
export GCR_MULTI_REGION="eu.gcr.io"
export GCR_REGION="europe-west1"

docker push $GCR_MULTI_REGION/$GCP_PROJECT_ID/$DOCKER_IMAGE_NAME
```

## Cloud run

Finally, you need to make your api continuously avilable. Go to the GCP console, to Cloud Run, and enable the service. You might also have to enable Cloud Run API.

```bash
export GCP_PROJECT_ID="PROJECT_ID"
export DOCKER_IMAGE_NAME="CONTAINER_NAME"
export GCR_MULTI_REGION="eu.gcr.io"
export GCR_REGION="europe-west1"

# Deploy your API to cloud run
gcloud run deploy --image $GCR_MULTI_REGION/$GCP_PROJECT_ID/$DOCKER_IMAGE_NAME --platform managed --region $GCR_REGION
```
