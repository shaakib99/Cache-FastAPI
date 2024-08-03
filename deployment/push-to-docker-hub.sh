#!/bin/bash 

set -e

DOCKER_HUB_USERNAME=""
DOCKER_HUB_PASSWORD=""
DOCKER_HUB_IMAGE=""
REMOTE_DOCKER_HUB_REPO=""
TAG=""

echo "Login to docker hub"
echo "$DOCKER_HUB_PASSWORD" | docker login -u $DOCKER_HUB_USERNAME --password-stdin

echo "Building image"
docker build -t $DOCKER_HUB_IMAGE ..

echo "Tagging image"
docker tag $DOCKER_HUB_IMAGE $REMOTE_DOCKER_HUB_REPO

echo "Pushing image"
docker push $DOCKER_HUB_IMAGE:$TAG

echo "Done"