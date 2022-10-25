FROM gcr.io/buildpacks/gcp/run:v1
USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
  libgomp1 && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

USER cnb