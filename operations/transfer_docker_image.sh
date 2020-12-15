#!/bin/bash

IMAGE_TAG=$1

if [[ -z $IMAGE_TAG ]]; then
  echo "error: IMAGE_TAG argument missing"; exit 1
fi

if [[ -z $HASHI_VAGRANT_REPO_DIRECTORY ]]; then
  echo "error: HASHI_VAGRANT_REPO_DIRECTORY env variable must be set"; exit 1
fi

docker image inspect $IMAGE_TAG > /dev/null 2>&1

if [[ $? != 0 ]]; then
  echo "error inspecting docker image, does '$IMAGE_TAG' exist?"; exit 1
fi


TARBALL_FILEPATH="$HASHI_VAGRANT_REPO_DIRECTORY/operations/docker_tarballs/$IMAGE_TAG.tar.gz"

rm -f $TARBALL_FILEPATH
docker image save -o $TARBALL_FILEPATH $IMAGE_TAG


CLIENT_NODE_NAMES=$(python -c '
import json
from os import environ
config_fp = environ["HASHI_VAGRANT_REPO_DIRECTORY"] + "/build_vagrant/conf/vagrant-cluster.json"
with open(config_fp) as file:
    config_data = json.loads(file.read())
client_names = [di["name"] for di in config_data if di["node_type"] == "hashi_client"]
print(" ".join(client_names))
')


cd $HASHI_VAGRANT_REPO_DIRECTORY/build_vagrant

for client_vm_name in $CLIENT_NODE_NAMES; do
  echo "loading tarball for $IMAGE_TAG on: $client_vm_name"
  vagrant ssh $client_vm_name -c "sudo docker load -i /docker_tarballs/$IMAGE_TAG.tar.gz; sudo docker tag $IMAGE_TAG nomad/$IMAGE_TAG"
done


rm -f $TARBALL_FILEPATH