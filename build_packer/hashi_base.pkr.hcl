
variable "hashi_vagrant_repo_directory" {}

variable "hashi_common_repo_directory" {}


source "vagrant" "example" {
  communicator = "ssh"
  source_path = "${var.hashi_vagrant_repo_directory}/build_packer/ubuntu2004.box"
  provider = "virtualbox"
  add_force = true
  output_dir = "${var.hashi_vagrant_repo_directory}/build_packer/base_image"
}

build {
  sources = ["source.vagrant.example"]

  #"sudo apt-get --yes --force-yes -o Dpkg::Options::='--force-confdef' -o Dpkg::Options::='--force-confold' upgrade",

  provisioner "shell" {
    environment_vars = [
      "DEBIAN_FRONTEND=noninteractive"
    ]
    inline = [

      "sudo apt-get update -y",
      #"sudo apt-get upgrade -y",

      "sudo apt install -y apt-transport-https ca-certificates",
      "sudo apt install -y gnupg-agent curl vim software-properties-common net-tools",
      "sudo apt install -y zip unzip npm nodejs jq python3-pip python3-testresources sshpass",

      "sudo apt autoremove -y",
      "sudo apt-get update -y"
    ]
  }

  provisioner "shell" {
    inline = [
      "sudo mkdir -p /home/vagrant",
      #"sudo useradd --system --home /home/vagrant --shell /bin/false vagrant",
      "sudo useradd --system --home /home/ubuntu --shell /bin/false ubuntu",

      "sudo mkdir -p /home/vagrant/scripts",
      "sudo mkdir -p /home/vagrant/services",
      "sudo chown vagrant:vagrant /home/vagrant/scripts",
      "sudo chown vagrant:vagrant /home/vagrant/services",

      "sudo mkdir -p /home/vagrant/.docker/"  # should this be copied to /home/root/.docker?
    ]
  }

  provisioner "file" {
    source = "${var.hashi_common_repo_directory}/build/vm_image/installation_scripts/" # trailing slash is important (https://www.packer.io/docs/provisioners/file.html#directory-uploads)
    destination = "/home/vagrant/scripts"
  }

  provisioner "file" {
    source = "${var.hashi_common_repo_directory}/services/"
    destination = "/home/vagrant/services"
  }

  provisioner shell {
    inline = [

      "sudo chmod +x -R /home/vagrant/scripts/",

      "sudo /home/vagrant/scripts/install-docker.sh",

      "sudo cp /home/vagrant/scripts/hashicorp-sudoers /etc/sudoers.d/hashicorp-sudoers",
      "sudo -H pip3 install -r /home/vagrant/scripts/python-requirements.txt",

      "sudo /home/vagrant/scripts/install-ansible__vagrant.sh",

      "sudo /home/vagrant/scripts/install-consul.sh",
      "sudo /home/vagrant/scripts/install-consul-template.sh",
      "sudo /home/vagrant/scripts/install-go-discover.sh",
      "sudo /home/vagrant/scripts/install-nomad.sh",
      "sudo /home/vagrant/scripts/install-vault.sh",
      # removed for vagrant: stackdriver, fluentd, ntp
    ]
  }
}