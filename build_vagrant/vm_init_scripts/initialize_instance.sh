#!/bin/bash


mv /tmp/scripts /scripts

export HOSTING_ENV=vagrant
export INSTANCE_CONFIG_FILEPATH="/script/build_vagrant/conf/vagrant-cluster.json"
export PROJECT_INFO_FILEPATH="/scripts/build_vagrant/conf/project-info.json"

{
  echo "HOSTING_ENV=$HOSTING_ENV"
  echo "INSTANCE_CONFIG_FILEPATH=$INSTANCE_CONFIG_FILEPATH"
  echo "PROJECT_INFO_FILEPATH=$PROJECT_INFO_FILEPATH"
} >> /etc/environment


/scripts/build/vm_image/init_scripts/initialize_instance__common.sh
