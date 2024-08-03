#!/bin/bash 

set -e

DOCKER_HUB_USERNAME="${DOCKER_HUB_USERNAME}"
DOCKER_HUB_PASSWORD="${DOCKER_HUB_PASSWORD}"
LOCAL_DOKER_IMAGE_TAG="${LOCAL_DOKER_IMAGE_TAG}"
REMOTE_DOCKER_HUB_REPO="${REMOTE_DOCKER_HUB_REPO}"
TAG="latest"

echo "Hello $DOCKER_HUB_USERNAME"
echo "Password $DOCKER_HUB_PASSWORD"

echo "Login to docker hub"
echo "$DOCKER_HUB_PASSWORD" | docker login -u $DOCKER_HUB_USERNAME --password-stdin

echo "Building image"
docker build -t $LOCAL_DOKER_IMAGE_TAG ..

echo "Tagging image"
docker tag $LOCAL_DOKER_IMAGE_TAG $REMOTE_DOCKER_HUB_REPO

echo "Pushing image"
docker push $REMOTE_DOCKER_HUB_REPO:$TAG

echo "Done"