#!/bin/bash


if [[ -z $HASHI_VAGRANT_REPO_DIRECTORY ]]; then
  echo "error: HASHI_VAGRANT_REPO_DIRECTORY env variable must be set"; exit 1
fi

if [[ -z $HASHI_COMMON_REPO_DIRECTORY ]]; then
  echo "error: HASHI_COMMON_REPO_DIRECTORY env variable must be set"; exit 1
fi


BASE_IMAGE_FILEPATH="$HASHI_VAGRANT_REPO_DIRECTORY/build_packer/base_image/package.box"

if [ ! -f "$BASE_IMAGE_FILEPATH" ]; then
  $HASHI_VAGRANT_REPO_DIRECTORY/build_packer/build_base_image.sh
  if [ ! -f "$BASE_IMAGE_FILEPATH" ]; then
    echo "failed to build base image"
    exit 1
  fi
fi


# for vagrant, assuming only 1 vault server at 172.20.20.13  (todo: fetch this from build_vagrant/conf/vagrant-cluster.json)
export HOSTING_ENV=vagrant

if [[ ! -f "/tmp/ansible-data/vault-tls-certs.zip" ]]; then
  $HASHI_COMMON_REPO_DIRECTORY/services/vault/init/tls-certs/create_vault_tls_certs.sh
fi

cd "$HASHI_VAGRANT_REPO_DIRECTORY/build_vagrant"
vagrant destroy -f
sleep 2
vagrant up


vagrant ssh hashi-server-1 -c "cd /scripts/build/ansible; ./bootstrap_cluster_services.sh"

# for some reason, Traefik isn't getting started by the ansible playbook? So retry it here.
vagrant ssh traefik-1 -c 'nomad job run /etc/traefik/traefik.nomad'

rm -rf /tmp/ansible-data/vault-tls-certs.zip


# to clear vagrant cache run:
# rm -rf ~/.vagrant.d/boxes/*
# rm -rf ~/VirtualBox\ VMs/*
