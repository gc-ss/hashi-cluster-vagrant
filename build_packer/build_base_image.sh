#!/bin/bash


UBUNTU_IMAGE_FILEPATH="$HASHI_VAGRANT_REPO_DIRECTORY/build_packer/ubuntu2004.box"
PACKER_DIR="$HASHI_VAGRANT_REPO_DIRECTORY/build_packer"

cd $PACKER_DIR || exit


if [ ! -f "$UBUNTU_IMAGE_FILEPATH" ]; then
  wget https://app.vagrantup.com/generic/boxes/ubuntu2004/versions/3.1.2/providers/virtualbox.box -o "./ubuntu2004.box"
fi


rm -rf "$PACKER_DIR/base_image"


packer build -force \
   -var="hashi_vagrant_repo_directory=$HASHI_VAGRANT_REPO_DIRECTORY" \
   -var="hashi_common_repo_directory=$HASHI_COMMON_REPO_DIRECTORY" \
   "$PACKER_DIR/hashi_base.pkr.hcl"
