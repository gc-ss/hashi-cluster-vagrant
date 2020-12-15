## Consul-Nomad-Vault cluster for Vagrant

**hashi-cluster-vagrant** is a pre-configured cluster for running Hashicorp's Consul, Nomad and Vault on locally on Vagrant VMs. It simulates a production cluster, operating similarly to its sister **hashi-cluster-gcp**.

It is designed to get you up and running quickly with minimal configuration and sensible defaults. No prior knowledge of Consul, Nomad, Vault or Vagrant is required.

**NOTE:** traefik's upstream connection to the service mesh is currently broken. I expect to fix this very soon.

### Installation Requirements:

* Virtualbox: https://www.virtualbox.org/wiki/Downloads
* Vagrant: https://www.vagrantup.com/docs/installation
* Terraform: https://learn.hashicorp.com/tutorials/terraform/install-cli


### Setup

Create a directory and clone the **hashi-cluster-vagrant** and **hashi-cluster-common** repos.

```
$ mkdir hashi-cluster/
$ cd hashi-cluster/
$ git clone https://github.com/rossrochford/hashi-cluster-vagrant.git
$ git clone https://github.com/rossrochford/hashi-cluster-common.git
```

#### Configuring the cluster 

By default, the cluster is configured to launch seven virtual machines: 

* `3` Consul/Nomad servers - stores the cluster state
* `1` Vault server - stores sensitive secrets
* `2` Consul/Nomad clients - runs your services
* `1` Traefik server  - receives HTTP requests and routes these to services

You can modify this in `build_vagrant/conf/vagrant-cluster.json`.

Things to keep in mind:

* Some IP addresses (Vault and Traefik) have been hard-coded and won't pickup up your config changes. I will fix this eventually.
* There are `3` hashi-servers by default. For local development you typically won't change this. There should ever only be `3`, `5` or `7` hashi-servers. If you change this, be sure to also update *num_hashi_servers* in `project-info.json`.
* It's common to add more Consul/Nomad clients, these VMs run your services. To add a client, simply copy-paste the config for *hashi-client-1* and give it a unique name and IP address. You'll want to do this before initializing the cluster, I haven't yet scripted a way to add clients to a running cluster on the fly.


#### Initializing the cluster

```
# set these environment variables to your repository directory paths
$ export HASHI_VAGRANT_REPO_DIRECTORY="$(pwd)/hashi-cluster-vagrant" 
$ export HASHI_COMMON_REPO_DIRECTORY="$(pwd)/hashi-cluster-common"

# run the main init script, this takes a while the first time
$ cd hashi-cluster-vagrant/
$ ./initialize_hashi_cluster.sh

# modify your hosts file
echo "127.0.0.1 traefik.localhost" >> /etc/hosts
echo "127.0.0.1 consul.localhost" >> /etc/hosts
echo "127.0.0.1 nomad.localhost" >> /etc/hosts
```

When the cluster has successfully initialized you will see some tokens printed to the console:

```
consul bootstrap token:                         4712dcf0-7ac8-4c17-e4c5-f816f611dccd
consul gossip encryption key:                   xrg1U5nKnrBG72l0ejy0pmkbY3M4Gdf5OpaI

consul UI token (read/write):                   689d66e0-3174-7f5e-3679-22080633f124
consul UI token (read-only):                    ae375762-606f-b7f7-fcf7-50fc32dc320a

vault root token:                               s.2vDe3uZ1JWidKS1xUsSYi7Y0
vault write-only token:                         s.tv1XD45e22QW6jfSkg3zxwfI
vault unseal key:                               Uwon8UhjsO7IYgksbrmmEJ96rAYkOvgd3iM4

Connection to 127.0.0.1 closed.
```

Dashboards for Traefik, Consul and Nomad will be accessible at:

* http://traefik.localhost:8085/dashboard
* http://consul.localhost:8085/ui 
* http://nomad.localhost:8085/ui

The Consul dashboard requires that you log in with your Consul UI read/write token.  If everything is working correctly, you should see your services in the Consul UI: `consul`, `nomad-server`, `nomad-client`, `traefik`, `vault-server`. If any of these are missing, wait 5 minutes and refresh the page.


#### Deploy your first service

To deploy a service to the cluster, the steps are identical to hashi-cluster-gcp: https://gcp-hashi-cluster.readthedocs.io/5_deploy_your_first_service.html


#### Destroying the cluster

```
$ cd build_vagrant/
$ vagrant destroy -f
```
